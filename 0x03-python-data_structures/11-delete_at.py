#!/usr/bin/python3
# deletes item at specific position in the list

def delete_at(my_list=[], idx=0):
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
