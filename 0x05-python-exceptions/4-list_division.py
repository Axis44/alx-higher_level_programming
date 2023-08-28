#!/usr/bin/python3
# divide element by elements
def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for n in range(list_length):
        try:
            div = my_list_1[n] / my_list_2[n]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            n_list.append(div)
    return n_list
