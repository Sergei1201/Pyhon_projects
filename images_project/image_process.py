import os
import sys
from PIL import Image

# Get file names from the current directory
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# Check if the ouput folder does not exist, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through images that are located in images directory, process them and put those into ouput directory
for filename in os.listdir(image_folder):
    # Create an instance of Image class and use its methods
    image = Image.open(f'{image_folder}{filename}', 'r')
    # Clean image's name
    clean_name = os.path.splitext(filename)[0]
    # Save the images in any preferable format
    image.save(f'{output_folder}{clean_name}.png', 'png')
print('All the images have been processed successfully!')
