---
description: Compiles LaTex project to Word using Pandoc then also saves the Word document to markdown original.md
model: claude-opus-4-5
---

First, check git stage for main.docx changes if there are changes exit this command and tell the user they have unsaved changes to the Word document.

Second, if git head indeed has nothing to commit, move the main.docx to backups folder and rename it to the head commit id. If backups folder doesn't exist, make it.

Third, recursively look into all files in ./src folder and create the appropriate pandoc command for the tex, references, figures, images and template. Compile the LaTeX to Word as "main.docx". Recall, don't run pandox if main.docx is staged or has git diffs. Instead prompt the user to save changes.

Fourth, convert the new Word document main.docx to "original.md" as markdown. We will use original.md later.