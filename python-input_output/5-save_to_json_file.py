#!/usr/bin/python3
"""function that writes an Object to a text file,
using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    ''' module save_to_json_file
    accepts Python object and sends JSON representation to file
    '''
    try:
        # Convert set to list to make it JSON serializable
        if isinstance(my_obj, set):
            raise TypeError("Object of type set is not JSON serializable")

        with open(filename, "w") as f:
            f.write(json.dumps(my_obj))
    except TypeError as e:
        print(f"[TypeError] {e}")
    except PermissionError as e:
        print(f"[PermissionError] {e}")
