# Clear neighboring terms around sign-column highlights

- Recorded at: 2026-11-15T05:37:22-08:00
- Observed work interval: 2026-11-15T05:35:08-08:00/2026-11-15T05:37:22-08:00 (134 seconds of regression authoring and spacing correction, including overlapping independent-video review and a wait for the red check). The earlier visual report's exact timestamp was not recorded here.
- Participants: OpenAI Codex, GPT-6 (root visual inspection and failing-test execution; delegated regression and spacing fix); Tomas Ortega (video-quality requirements).

## Context and decision

The first rendered [Parity of Sign Columns scene](../videos/halve_sign_sums.py),
prepared in the [production record](2026-11-15-053146-prepare-halve-sign-sums-video.md),
showed its coefficient-selection rectangles crossing neighboring plus glyphs.
Add an [actual-scene geometry regression](../videos/test_halve_sign_sums.py)
before correcting the source. The agreed observation point is the scene's
public `show` path, using its real constructed mathematics and rectangles.

## Rationale

Capture all four original polynomial rows and their four highlight rectangles.
Require at least 0.1 scene units between each rectangle and both neighboring
prefix/suffix terms. This checks the observed layout rather than duplicating
coordinates or manufacturing a separate specimen. Mock only the narration/audio
boundary; run the real scene construction up to the selected highlight.

After the failing check, increase only the opening rows' arrangement spacing
from 0.06 to 0.22. The highlight padding remains 0.09. Also increase the inner
spacing between the two modulo-two pairs from 0.12 to 0.25, leaving room for
their two 0.08-padded rectangles. No mathematical formula, narration, timing,
other arrangement, or shared helper changes.

## Evidence and outcome

Root ran the regression before the source fix: eight failed checks in
0.515 seconds, with all prefix/suffix gaps measured at −0.03 scene units.
This confirms the actual overlap. The two requested spacing changes are now
applied; source and test pass Ruff lint, formatting, and Python compilation.
The scene and test are frozen for root's green check and offline rerender.
The existing one-take narration is reused, and production hashes are not
refreshed against the superseded export. Final green-test and native-frame
outcomes must be recorded after they are observed.

## Report relevance

Records an observed production defect, a failing-first regression at the
actual rendering interface, and a minimal visual correction. This changes
spacing and selection clarity, not the coefficient parity proof.
