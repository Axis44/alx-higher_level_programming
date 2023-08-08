#!/usr/bin/python3
for z in range(122, 96, -1):
    if z % 2:
        z = z - 32
    print("{:c}".format(z), end="")
