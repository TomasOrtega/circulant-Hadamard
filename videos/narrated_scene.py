import os
from contextlib import contextmanager

from manimlib import Scene

from narration.speech import Narrator


class NarratedScene(Scene):
    def setup(self):
        super().setup()
        self.narrator = Narrator(offline=os.environ.get("NARRATION_OFFLINE") == "1")

    @contextmanager
    def narrate(self, text):
        clip = self.narrator.audio(text)
        started = self.time
        self.add_sound(str(clip.path))
        yield clip
        remaining = clip.duration - (self.time - started)
        if remaining > 0:
            self.wait(remaining)
