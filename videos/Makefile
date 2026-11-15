UV = uv run --locked --group narration --group video
SCENE ?= AchirdDemo
SOURCE ?= videos/achird_demo.py
export MPLCONFIGDIR := $(abspath .cache/matplotlib)

.PHONY: seed preview render render-4k check

seed:
	cd .. && $(UV) python -m narration.demo

preview: seed
	cd .. && NARRATION_OFFLINE=1 $(UV) python -m manimlib $(SOURCE) $(SCENE) -w -l --fps 15

render:
	cd .. && $(UV) python -m manimlib $(SOURCE) $(SCENE) -w --hd --fps 30

render-4k:
	cd .. && $(UV) python -m manimlib $(SOURCE) $(SCENE) -w --uhd --fps 30

check:
	cd .. && $(UV) python -m unittest discover -s narration -p 'test_*.py'
	cd .. && $(UV) python -m unittest discover -s videos -p 'test_*.py'
