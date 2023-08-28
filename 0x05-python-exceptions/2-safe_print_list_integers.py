#!/usr/bin/python3

# print first integers in list
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for n in range(x):
        try:
            print("{:d}".format(my_list[n]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    Return
