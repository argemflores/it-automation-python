#!/usr/bin/env python3

# Import Image module from PIL
from PIL import Image

# Open image
im = Image.open("Zagreus.jpg")

# Resize image to 860x480 pixels and save it as a new file
new_im = im.resize((860,480))
new_im.save("temp_Zagreus_resized_860x480.jpg")

# Rotate image by 90 degrees and save it as a new file
new_im = im.rotate(90)
new_im.save("temp_Zagreus_rotated_90deg.jpg")

# Rotate image by 180deg and resize it to 860x480 pixels as a new file
im.rotate(180).resize((860,480)).save("temp_Zagreus_flipped_180deg_and_resized_860x480.jpg")
