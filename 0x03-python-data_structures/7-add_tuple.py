#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    first_sum = a[0] + b[0]
    second_sum = a[1] + b[1]
    total = (first_sum, second_sum)
    return (total)
