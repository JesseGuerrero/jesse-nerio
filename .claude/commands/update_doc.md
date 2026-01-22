---
description: Converts main.docx to markdown updated.md then compares original.md to updated.md and updates main.tex made to updated in the diff.
model: claude-opus-4-5
---

First look at all files in src folder.

Second, check main.tex to see if it is in git stage or has differences in git diff. If indeed it is staged or has git diff then prompt the user there are unsaved changes in main.tex and stop this program.

Third, if main.tex is not staged and has no git diffs in its diff tree convert main.docx to updated.md. If updated.md exists, overwrite it.

Fourth, use git diff between updated.md and original.md and make changes to main.tex based on that diff. Recall original.md is the original and after we make updates we refer to updated.md

Keep to these principles:
- If a section, paragraph, sentence or word was deleted in the updated.md in the git diff, please also delete it in the LaTeX.
- If a citation was deleted also delete the citation in LaTeX
- Keep formatting of original main.tex, we are more trying to update content, not formatting
- Do keep citation formatting to be appropriate to the original main.tex
