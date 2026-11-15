import math
import os
from contextlib import contextmanager

from manimlib import Scene

from narration.speech import Narrator, Voice


class NarratedScene(Scene):
    narration_voice = Voice()
    narration_ssml = False

    def setup(self):
        super().setup()
        self._narration_started = None
        self.narrator = Narrator(
            voice=self.narration_voice,
            offline=os.environ.get("NARRATION_OFFLINE") == "1",
            ssml=self.narration_ssml,
        )

    @contextmanager
    def narrate(self, text):
        if self._narration_started is not None:
            raise RuntimeError(
                "Each scene uses one continuous narration. "
                "Put the full script in a single narrate() block."
            )
        clip = self.narrator.audio(text)
        started = self.time
        self._narration_started = started
        self.add_sound(str(clip.path))
        yield clip
        remaining = clip.duration - (self.time - started)
        if remaining > 0:
            self.wait(remaining)

    def wait_until_narration(self, seconds):
        if self._narration_started is None:
            raise RuntimeError("Start narration before waiting for a cue.")
        if not math.isfinite(seconds) or seconds < 0:
            raise ValueError("Narration cue must be finite and nonnegative.")
        remaining = self._narration_started + seconds - self.time
        if remaining > 0:
            self.wait(remaining)
