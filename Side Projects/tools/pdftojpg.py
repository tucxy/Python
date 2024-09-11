import os
from pdf2image import convert_from_path

# Define file paths
pdf_path = r"C:\Users\baneg\Downloads\dues (orientation 1).pdf"
output_folder = r"C:\Users\baneg\Downloads\paper scans of dues"

# Create the output directory if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Convert PDF to images
images = convert_from_path(pdf_path)

# Save each page as a separate JPEG file
for i, image in enumerate(images):
    image_path = os.path.join(output_folder, f"page_{i + 1}.jpg")
    image.save(image_path, 'JPEG')
