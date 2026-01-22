---
description: Create new blog posts from a glob list of *.pdf into ./blog/posts and place its indexed entry into ./blog/index.html
model: claude-opus-4-5
---

read ./blog/posts/what-is-the-computer-information-systems-major.html only that file. Also notice the folder ./blog/images and ./blog/posts 

Glob the first level of the ./blog folder and look for *.pdf

Read the PDFs one at a time and create a blog post of it in the exact words and image positions but while keeping the exact style of  ./blog/posts/what-is-the-computer-information-systems-major.html.

Place this blog entry of each pdf into ./blog/index.html but do it in the same chronological order already in ./blog/index.html

To extract the images use ./blog/images folder and also this "python ./extract_pdf_images.py PDF_PATH". Dont read or create any python scripts. Just run ./extract_pdf_images.py with the PDF path of each pdf one at a time as the argument and it will place the images in the ./blog/images path

So remember do one pdf at a time