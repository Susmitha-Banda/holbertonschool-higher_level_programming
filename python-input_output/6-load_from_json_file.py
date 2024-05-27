#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""

    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except PermissionError as e:
        print(f"[PermissionError] {e}")
