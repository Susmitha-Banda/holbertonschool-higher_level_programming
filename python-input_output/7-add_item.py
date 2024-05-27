#!/usr/bin/python3
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
