#!/usr/bin/python3
"""function that returns the JSON representation of an object (string):"""

import json


def to_json_string(my_obj):
    """Returns JSON representation of an object."""
    def convert(obj):
        if isinstance(obj, set):
            return list(obj)
        raise TypeError(f"Object of type {type(obj).__name__}
                        is not JSON serializable")

    return json.dumps(my_obj, default=convert)
