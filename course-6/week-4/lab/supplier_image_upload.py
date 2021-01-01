#!/usr/bin/env python3

import os
import requests

images_dir = 'supplier-data/images/'

# Get all image filenames
url = 'http://localhost/upload/'
imagenames = os.listdir(images_dir)
# print(filenames) # prints all files in the images directory, including README and LICENSE

# Process each file in the images directory
for imagename in imagenames:
    # Check file if .tiff image
    if imagename.endswith('.jpeg'):
        with open(os.path.join(images_dir, imagename), 'rb') as image:
            response = requests.post(url, files={'file': image})
            print(imagename, response.ok, response.status_code)
