#!/usr/bin/env python3

# Import libraries
import requests

# Sample data
url = 'https://www.google.com'
bad_url = 'https://www.google.com/bad_url_example'

# Send a get request, then print the first 300 characters in the response
response = requests.get(url)
print(response.text[:300])

# Send a get request with stream, then print the first 100 characters in the response
response = requests.get(url, stream=True)
print(response.raw.read()[:100])

##################################################

# Print request and some header data
print(response.request.headers['Accept-Encoding'])
print(response.headers['Content-Encoding'])

# Check response statuses
print(response.ok)
print(response.status_code)

# Check response before processing it further
# response = requests.get(bad_url)
# if not response.ok:
#     raise Exception("GET failed with status code {}".format(response.status_code))

# Use built-in status check instead of the manual checking above
# response = requests.get(bad_url)
# response.raise_for_status()

##################################################

# Create a sample get request with parameters
p = {"search": "grey kitten", "max_results": 15}
response = requests.get("https://example.com/path/to/api", params=p)
# Produces https://example.com/path/to/api?search=grey+kitten&max_results=15
print(response.request.url)

# Create another sample get request with a different set of parameters
p = {"description": "white kitten", "name": "Snowball", "age_months": 6}
response = requests.post("https://example.com/path/to/api", data=p)
# Produces https://example.com/path/to/api with the data in the request body
print(response.request.url)
print(response.request.body)

# Do the same actions above but use JSON as the format in the request body
p = {"description": "white kitten", "name": "Snowball", "age_months": 6}
response = requests.post("https://example.com/path/to/api", json=p)
print(response.request.url)
print(response.request.body)
