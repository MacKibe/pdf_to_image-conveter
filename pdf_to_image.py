import os
from pdf2image import convert_from_path

# Create a directory named '9' if it doesn't exist
output_dir = '17'
os.makedirs(output_dir, exist_ok=True)

# Convert PDF to list of images
images = convert_from_path('17.pdf')

# Save each image in the '9' directory as JPEG
for i, image in enumerate(images):
    image_path = os.path.join(output_dir, f'17-page_{i + 1}.jpg')
    image.save(image_path, 'JPEG')

