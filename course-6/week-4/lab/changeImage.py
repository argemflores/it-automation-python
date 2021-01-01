#!/usr/bin/env python3

import logging
import os
from PIL import Image

images_dir = 'supplier-data/images/'

# Get all image filenames
imagenames = os.listdir(images_dir)
# print(filenames) # prints all files in the images directory, including README and LICENSE

# Process each file in the images directory
for imagename in imagenames:
    # Check file if .tiff image
    if imagename.endswith('.tiff'):
        # print(filename) # prints filename ending in .tiff
        # Open image
        image = Image.open(os.path.join(images_dir, imagename))

        # Convert image to JPG then resize to 600x400
        image.convert('RGB').resize((600,400)).save(os.path.join(images_dir, imagename[:-5] + '.jpeg'))
        # print(imagename[:-5]) # prints the name of the file without the file extension
