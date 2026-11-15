"""Readable captions from exact-source words aligned to a single recording."""

import math
from html import escape

MAX_LINE = 42
MIN_DISPLAY_MS = 1000


def _lines(words):
    text = " ".join(words)
    if len(text) <= MAX_LINE:
        return [text], 0
    choices = []
    for split in range(1, len(words)):
        first, second = " ".join(words[:split]), " ".join(words[split:])
        if max(len(first), len(second)) <= MAX_LINE:
            cost = abs(len(first) - len(second)) / MAX_LINE
            choices.append((cost, [first, second]))
    if not choices:
        return None
    cost, lines = min(choices, key=lambda item: item[0])
    return lines, cost


def _timestamp(ms):
    return (
        f"{ms // 3600000:02}:{ms // 60000 % 60:02}:{ms // 1000 % 60:02}.{ms % 1000:03}"
    )


def make_vtt(words, duration):
    """Return WebVTT for {word, start, end} dictionaries, with seconds as times.

    Pass exact spoken-source tokens, including their punctuation and case, after
    alignment. Tokens must be whitespace-free and at most 42 visible characters.
    Starts must be ordered and all times must be finite and within duration.
    Overlapping word intervals are divided at the next caption's first word.

    Dynamic programming balances reading speed, sentence breaks, and at most two
    42-character lines. Short captions extend into available quiet time, capped
    by the next caption. One second is a soft minimum: very short clips or dense
    speech with no feasible line-constrained grouping can require shorter cues.
    """
    if not math.isfinite(duration) or duration < 0:
        raise ValueError("Caption duration must be finite and nonnegative.")
    limit = math.floor(duration * 1000)
    tokens, starts, ends = [], [], []
    previous = -1
    for entry in words:
        word, start, end = entry["word"], entry["start"], entry["end"]
        if (
            not isinstance(word, str)
            or not word
            or any(char.isspace() for char in word)
            or len(word) > MAX_LINE
        ):
            raise ValueError("Each caption word must contain 1–42 nonspace characters.")
        if (
            not math.isfinite(start)
            or not math.isfinite(end)
            or not 0 <= start <= end <= duration
            or start < previous
            or start >= duration
        ):
            raise ValueError(
                "Caption words need ordered, finite times within duration."
            )
        tokens.append(word)
        starts.append(min(limit, round(start * 1000)))
        ends.append(min(limit, round(end * 1000)))
        previous = start
    count = len(tokens)
    if not count:
        return "WEBVTT\n\n"

    best = [math.inf] * count + [0.0]
    following = [None] * count
    for first in range(count - 1, -1, -1):
        chars = 0
        for stop in range(first + 1, count + 1):
            chars += len(tokens[stop - 1]) + (stop > first + 1)
            if chars > 2 * MAX_LINE + 1:
                break
            wrapped = _lines(tokens[first:stop])
            if wrapped is None:
                continue
            lines, balance = wrapped
            next_start = starts[stop] if stop < count else limit
            end = min(
                next_start,
                max(max(ends[first:stop]) + 120, starts[first] + MIN_DISPLAY_MS),
            )
            elapsed = (end - starts[first]) / 1000
            if elapsed <= 0:
                continue
            reading_speed = chars / elapsed
            cost = 4 + balance + 0.35 * (elapsed - 3.2) ** 2
            cost += 0.18 * max(0, reading_speed - 18) ** 2
            cost += 5 * max(0, elapsed - 6) ** 2
            if elapsed < 1:
                cost += 50 + 80 * (1 - elapsed) ** 2
            punctuation = tokens[stop - 1].rstrip('"\u201d\u2019)')
            if punctuation.endswith((".", "?", "!")):
                cost -= 2
            elif punctuation.endswith((",", ";", ":")):
                cost -= 0.5
            else:
                cost += 2
            cost += sum(
                max(0, (starts[index + 1] - ends[index]) / 1000 - 0.7) * 5
                for index in range(first, stop - 1)
            )
            if cost + best[stop] < best[first]:
                best[first] = cost + best[stop]
                following[first] = stop, end, lines

    if following[0] is None:
        raise ValueError("Word timing and line limits leave no valid caption grouping.")
    output = ["WEBVTT\n"]
    first = 0
    while first < count:
        stop, end, lines = following[first]
        output.append(
            f"{_timestamp(starts[first])} --> {_timestamp(end)}\n"
            + "\n".join(escape(line, quote=False) for line in lines)
            + "\n"
        )
        first = stop
    return "\n".join(output)
