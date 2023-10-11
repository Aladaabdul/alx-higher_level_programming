#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_delete = []
    for k, v in a_dictionary.items():
        if v == value:
            key_delete.append(k)

    for key in key_delete:
        del a_dictionary[key]

    return a_dictionary
