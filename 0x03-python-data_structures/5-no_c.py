#!/usr/bin/python3
# removes character c and C from string

def no_c(my_string):
    new_str = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            new_str += char
    return (new_str)
