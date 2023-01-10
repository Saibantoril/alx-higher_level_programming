#!/usr/bin/python3
"""this module defines a string yo Json function"""

import json


def to_json_string(my_obj):
    """returns the JSON representation of  string object"""
    
    return json.dumps(my_obj)
