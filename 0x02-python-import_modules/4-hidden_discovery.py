#!/usr/bin/python3
if __name__ == "__main__":
    "" to print hidden_4 module names""
    import hidden_4
    for name = dir(hidden_4):
        if name[0] != '_' and name[1] != '_':
            print(name)
