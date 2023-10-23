#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    numbers = 0
    try:
        for i in my_list:
            if numbers >= x:
                break
            if type(i) is not str:
                print("{:d}".format(i), end="")
                numbers += 1
    except (IndexError, TypeError, ValueError):
        pass
    finally:
        print()
    return numbers
