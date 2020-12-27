#!/usr/bin/env python3

# Import libraries
import os
import requests

# URL to send feedback as POST request
feedback_dir = '/data/feedback'
url = 'http://104.198.166.70/feedback/'

# List of feedback attributes
attributes = ['title', 'name', 'date', 'feedback']

# Get all filenames from the feedback directory
filenames = os.listdir(feedback_dir)

# Process each feedback file
for filename in filenames:
    # Open file
    with open(feedback_dir + '/' + filename, 'r') as file:
        # Extract data from the file per line and store it to data dictionary
        data = {}
        for attribute in attributes:
            data[attribute] = file.readline().strip() # remove extra spaces/newlines
        # Send feedback as POST request
        response = requests.post(url, json=data)
        # Show results and raise status
        print(response.ok, response.status_code)
        # response.raise_for_status()
