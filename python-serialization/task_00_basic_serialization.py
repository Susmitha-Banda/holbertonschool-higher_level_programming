#!/usr/bin/env python3
"""
creating a Python module that provides functionality to
serialize (convert to JSON and save to a file) and
deserialize (read from a JSON file and recreate a Python dictionary) data.
"""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize data to JSON and save it to the specified file."""
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load JSON data from the specified file and deserialize it."""
    with open(filename, "r") as f:
        return json.loads(f)
