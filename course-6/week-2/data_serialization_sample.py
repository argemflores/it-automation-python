#!/usr/bin/env python3

# Import libraries
import json
import yaml

# Example data
people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": {
            "office": "802-867-5309",
            "cell": "802-867-5310"
        },
        "department": "IT Infrastructure",
        "role": "Systems Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": {
            "office": "684-348-1127"
        },
        "department": "IT Infrastructure",
        "role": "IT Specialist"
    },
]

# Export data to json
with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)

# Export data to yaml
with open('people.yaml', 'w') as people_yaml:
    yaml.safe_dump(people, people_yaml)

# Transform json to Python objects
with open('people.json', 'r') as people_json:
    people = json.load(people_json)
    print(people)