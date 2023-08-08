#!/usr/bin/python3
def uppercase(str):
    for t in str:
        if ord("a") <= ord(t) <= ord("z"):
            t = chr(ord(t) - 32)
        print("{:s}".format(t), end="")
    print()

