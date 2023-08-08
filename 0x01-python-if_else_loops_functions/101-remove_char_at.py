#!/usr/bin/python3
def remove_char_at(str, n):
    t = 0
    new_str = ""
    for ch in str:
        if t != n:
            new_str += ch
        t += 1
    return
