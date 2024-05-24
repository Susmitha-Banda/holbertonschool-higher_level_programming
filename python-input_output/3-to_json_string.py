#!/usr/bin/python3
"""function that returns the JSON representation of an object (string):"""

import json


def to_json_string(my_obj):
    """module to_json_strin
     returns JSON representation"""
    if isinstance(my_obj, set):
        '''the json.dumps() function in Python does not support
        serializing set objects directly to JSON.'''
        try:
            return json.dumps(list(my_obj))
        except Exception:
            raise TypeError("Object of type set is not JSON serializable")

    return json.dumps(my_obj)
