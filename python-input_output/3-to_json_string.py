#!/usr/bin/python3
"""function that returns the JSON representation of an object (string):"""

import json


def to_json_string(my_obj):
    """Returns JSON representation of an object."""
    def convert(obj):
        if isinstance(obj, set):
            raise TypeError("Object of type set is not JSON serializable")
        return my_obj

    return json.dumps(my_obj, default=convert)
