#!/usr/bin/python3
"" to print argument list with numnberX""
if __name__ == "__main__":
    import sys

    arg = sys.argv
    size = len(arg) - 1

    if size > 1:
        print("{} arguments:".format(size))
        for j in range(1, size + 1):
            print("{}: {}".format(j, arg[j]))

    elif size == 0:
        print("{} arguments.".format(size))

    else:
        print("{} argument:".format(size))
        print("{}: {}".format(size, arg[1]))
