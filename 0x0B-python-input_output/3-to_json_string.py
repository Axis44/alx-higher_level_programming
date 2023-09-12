#!/usr/bin/python3
def write_file(filename="", text=""):
    """ writes the string to a text file (UTF8)  """

    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
