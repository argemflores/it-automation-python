#!/usr/bin/env python3

# Import needed libraries
import os
import requests

# Defined upload URL and descriptions directory
url = 'http://localhost/fruits/'
desc_dir = 'supplier-data/descriptions/'

# List all text files in the descriptions directory
filenames = os.listdir(desc_dir)
# print(descnames) # prints list of descriptions as text files

# Extract and upload contents of each description file
for filename in filenames:
    # print('>>>', filename)
    data = {}
    # Open description file for reading
    with open(os.path.join(desc_dir, filename), 'r') as file:
        # Retrieve data from the text file for each field
        for field in ['name', 'weight', 'description']:
            # print(field, file.readline())
            # Get content from the file
            line = file.readline().strip()
            # Convert to integer if field is weight
            if field == 'weight':
                line = int(line[:-4])
            # print(field, line)
            data[field] = line
        # print('image_name', os.path.splitext(filename)[0] + '.jpeg')
        data['image_name'] = os.path.splitext(filename)[0] + '.jpeg'
        # print(data)
        response = requests.post(url, data=data)
        print(filename, response.ok, response.status_code)
