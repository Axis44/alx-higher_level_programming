#!/usr/bin/python3
if __name__ == "__main__":
    "" adds all arguments""
    import sys
    result = 0
     for t in range(len(sys.argv) - 1):
        result += int(sys.argv[t + 1])
    print("{}".format(total))
