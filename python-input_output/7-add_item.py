#!/usr/bin/python3
"""
This script adds all command line arguments to a Python list,
and then saves them to a file named add_item.json.

- If the file doesn’t exist, it should be created.
- The list is saved as a JSON representation in the file add_item.json.
"""

import sys
import os

# Import the required functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


# Define the filename
filename = "add_item.json"

# Load existing items if the file exists, otherwise start with an empty list
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add command line arguments to the list
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, filename)
