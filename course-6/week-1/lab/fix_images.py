#!/usr/bin/env python3

# Import libraries and modules
from PIL import Image
import os

# Get current working directory
cwd = os.getcwd()

# Process each image from the list in the text file
with open("list_images.txt", "r") as file:
    for filename in file.readlines():
        filename = filename.strip() # remove extra spaces and newlines
        # Open file
        img = Image.open(cwd + "/images/" + filename)
        # Rotate image by 90 deg, resize to 128x128, convert to JPEG, and save to another folder
        img.rotate(90).resize((128,128)).convert("RGB").save("/opt/icons/" + filename + ".jpg")
    file.close() # close text file
