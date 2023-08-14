#!/usr/bin/python3
# replaces element of list at specific line

def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
