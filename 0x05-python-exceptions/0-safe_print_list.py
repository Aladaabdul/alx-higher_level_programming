#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    numbers = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end= '')
            numbers += 1
    except IndexError:
            pass
    print()
    return numbers


