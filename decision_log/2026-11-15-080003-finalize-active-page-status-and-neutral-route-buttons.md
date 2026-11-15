# Finalize active page status and neutral route buttons

- Recorded at: 2026-11-15T08:00:03-08:00
- Observed implementation and website-validation interval:
  2026-11-15T07:57:46-08:00/2026-11-15T08:00:03-08:00 (137 seconds).
- Participants: Tomas Ortega (requested wording, status, button, commit and
  push changes); OpenAI Codex, GPT-6 (implementation and checks).

## Context and decision

Following the [content-completeness review](2026-11-15-075252-review-actual-mathematical-content-completeness.md),
the user requested correcting the General Proof guide's stale deferral wording,
setting all current draft flags to false, fixing the initially highlighted
example-route button, then committing and pushing.

Update the guide's final reference sentence to link to the developed order
restriction and Delta theorem proof nodes. Set `draft: false` on the 48 active
nodes and both supplementary reading guides. Historical archived pages retain
their original metadata. Remove the explicit `primary` prop from the homepage's
example-route button so both reading routes use the existing neutral style.

This user-directed status change supersedes the choice to retain active draft
metadata in the [video acceptance record](2026-11-15-072130-accept-all-scripted-node-videos.md)
and the [earlier status inventory](2026-11-15-074954-clarify-mathematical-draft-labels.md).
The quoted historical statuses in those records remain accurate for their times.

## Rationale

The guide's deferral sentence predates the developed child arguments. Updating
its links reflects the current hierarchy without expanding the mathematics.
The user approved the editorial completion status while retaining the cited
cyclotomic inputs. That status change is not new mathematical verification.

The button issue came from its explicit primary appearance, which supplied a
filled theme background before interaction. Reuse the ordinary NodeButton
style, preserving its existing hover and keyboard-focus feedback. The
[diagnosing-bugs skill](file:///Users/to1717/.codex/plugins/cache/mattpocock/mattpocock-skills/1.3.2/skills/engineering/diagnosing-bugs/SKILL.md)
informed the regression-first diagnosis. Ranked hypotheses were explicit
primary styling, a first-link CSS rule, and automatic focus; the first was
confirmed. A targeted rendered-homepage test was the minimal useful feedback
loop, so broader instrumentation was unnecessary.

## Evidence and outcome

- Before the fix, the new reading-route appearance regression failed twice:
  the example button had a filled background/white text while the general
  button had the neutral text/interaction classes. Removing only `primary`
  made the same test pass.
- All 184 website tests pass (9,352 assertions across 18 files), including
  guide links, navigation, mathematics rendering, and existing media.
- `make -C website` builds 50 active pages and the compiled styles.
  The website parser independently confirms `draft: false` on all 50.
- Browser-host discovery was unavailable. Native Firefox preview of the
  rebuilt homepage succeeded and visibly showed both routes without a
  default filled highlight.
- The changes include the three preceding inquiry/audit decision records.
  Final lint, commit, and push follow this implementation record.

## Report relevance

Records user-approved completion metadata and a navigation appearance fix.
The mathematical arguments and existing cited dependencies are retained;
no new proof, computation, or formal verification is claimed.

Final repository validation recorded at 2026-11-15T08:00:30-08:00: `uv run --locked prek -a --quiet` and staged whitespace checks both passed. Commit and push follow.
