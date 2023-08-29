#!/usr/bin/python3

import sys
# execute function


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return (result)

    except Exception:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
