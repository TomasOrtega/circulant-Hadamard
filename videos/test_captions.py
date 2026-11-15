import html
import unittest

from videos.captions import make_vtt, spoken_paragraphs


def parse_vtt(source):
    def seconds(value):
        hours, minutes, seconds = value.split(":")
        return int(hours) * 3600 + int(minutes) * 60 + float(seconds)

    result = []
    for block in source.strip().split("\n\n")[1:]:
        timing, *lines = block.splitlines()
        start, end = timing.split(" --> ")
        result.append((seconds(start), seconds(end), [html.unescape(v) for v in lines]))
    return result


def timed_words(text, interval=0.32):
    return [
        {"word": word, "start": i * interval, "end": (i + 1) * interval - 0.02}
        for i, word in enumerate(text.split())
    ]


class CaptionTests(unittest.TestCase):
    def test_internal_ssml_breaks_separate_caption_words(self):
        source = (
            '<speak><p>Zero.<break time="700ms"/>Consequently, keep '
            '<emphasis>each</emphasis> word.</p><p>One.<break time="1s"/>'
            "The next statement.</p></speak>"
        )
        self.assertEqual(
            spoken_paragraphs(source),
            ["Zero. Consequently, keep each word.", "One. The next statement."],
        )

    def test_short_sentence_tail_is_not_a_flashing_standalone_caption(self):
        text = "The coefficient moves around our cyclic row and then comes back to one."
        words = timed_words(text)
        words[-1]["end"] = words[-1]["start"] + 0.1
        cues = parse_vtt(make_vtt(words, words[-1]["end"] + 0.9))
        self.assertTrue(cues)
        self.assertTrue(all(end - start >= 0.999 for start, end, _ in cues))
        self.assertTrue(all(" ".join(lines) != "one." for _, _, lines in cues))

    def test_long_source_is_wrapped_and_preserved_without_overlaps(self):
        text = (
            "The coefficients of the polynomial encode every cyclic correlation. "
            "Collect the terms whose exponents agree modulo the order of the group."
        )
        words = timed_words(text)
        duration = words[-1]["end"] + 1
        cues = parse_vtt(make_vtt(words, duration))
        self.assertEqual(" ".join(line for _, _, lines in cues for line in lines), text)
        previous_end = 0
        for start, end, lines in cues:
            self.assertGreaterEqual(start, previous_end)
            self.assertLessEqual(end, duration)
            self.assertGreaterEqual(end - start, 0.999)
            self.assertLessEqual(len(lines), 2)
            self.assertTrue(all(len(line) <= 42 for line in lines))
            previous_end = end

    def test_available_quiet_time_extends_a_short_utterance(self):
        words = [
            {"word": "One.", "start": 1.0, "end": 1.1},
            {"word": "Two.", "start": 3.0, "end": 3.2},
        ]
        cues = parse_vtt(make_vtt(words, 5))
        self.assertTrue(all(end - start >= 1 for start, end, _ in cues))
        self.assertEqual(cues[0][0], 1)
        self.assertLessEqual(cues[-1][1], 5)

    def test_markup_characters_are_displayed_as_spoken_text(self):
        text = "Use H < n & keep h > zero."
        cues = parse_vtt(make_vtt(timed_words(text), 4))
        self.assertEqual(" ".join(line for _, _, lines in cues for line in lines), text)

    def test_a_subsecond_clip_can_have_a_subsecond_caption(self):
        cues = parse_vtt(make_vtt([{"word": "One.", "start": 0, "end": 0.3}], 0.5))
        self.assertEqual(cues, [(0.0, 0.5, ["One."])])

    def test_invalid_timestamps_and_unbreakable_long_tokens_are_rejected(self):
        for words, duration in [
            ([{"word": "a" * 43, "start": 0, "end": 1}], 2),
            ([{"word": "one", "start": -1, "end": 1}], 2),
            ([{"word": "one", "start": 0, "end": 3}], 2),
            ([{"word": "one", "start": 1, "end": 0}], 2),
            ([{"word": "one", "start": 0, "end": 1}], float("nan")),
        ]:
            with (
                self.subTest(words=words, duration=duration),
                self.assertRaises(ValueError),
            ):
                make_vtt(words, duration)


if __name__ == "__main__":
    unittest.main()
