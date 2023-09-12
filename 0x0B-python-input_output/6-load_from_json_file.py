#!/usr/bin/python3

import json


def from_json_string(my_str):
    """ to returns an Python data represented by a JSON """
    return json.loads(my_str)
