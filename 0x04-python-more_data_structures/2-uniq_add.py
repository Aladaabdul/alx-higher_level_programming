#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    x = set(my_list)
    for i in x:
        result = result + i
    return result
