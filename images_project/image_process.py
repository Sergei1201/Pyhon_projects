import os
import sys
from PIL import Image

# Get file names from the current directory
images_folder = sys.argv[1]
output_folder = sys.argv[2]

# If output folder does not exist, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(output_folder)

# Loop through all images that are located in images directory and move them into outpu directory
for filename in os.listdir(images_folder):
    image = Image.open(f'{images_folder}{filename}', 'r')
    clean_name = os.path.splitext(filename)[0]
    image.save(f'{output_folder}{clean_name}.png', 'png')
    print(f'All images have been processed, {image}')
