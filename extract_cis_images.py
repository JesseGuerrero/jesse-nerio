import fitz  # PyMuPDF
import os

pdf_path = r"blog\What is the Computer Information Systems major_ -.pdf"
output_dir = "blog/images"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Open the PDF
pdf_document = fitz.open(pdf_path)

image_count = 0
for page_num in range(len(pdf_document)):
    page = pdf_document[page_num]
    image_list = page.get_images(full=True)

    for img_index, img in enumerate(image_list):
        xref = img[0]
        base_image = pdf_document.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]

        # Save the image
        image_filename = f"{output_dir}/cis-major-img-{image_count}.{image_ext}"
        with open(image_filename, "wb") as image_file:
            image_file.write(image_bytes)

        print(f"Extracted: {image_filename} from page {page_num + 1}")
        image_count += 1

pdf_document.close()
print(f"\nTotal images extracted: {image_count}")
