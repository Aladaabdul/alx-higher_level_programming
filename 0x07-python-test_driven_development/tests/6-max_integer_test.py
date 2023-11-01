#!/usr/bin/python3
"""
Unittest for max_integer([..])

"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    
    """Test case for max_integer"""

    def test_max_integer(self):
        self.assertEqual(max_integer([10, 100, -2, 5]), 100)
    
    def test_max_negative(self):
        self.assertEqual(max_integer([-5, -100, -1, -2]), -1)

    def test_max_none(self):
        self.assertEqual(max_integer([]), None)

    def test_equal(self):
        self.assertEqual(max_integer([100, 100, 100, 100]), 100)

    def max_first(self):
        self.assertEqual(max_integer([10, 5, 3, 1]), 10)

    def max_last(self):
        self.assertEqual(max_integer([2, 5, 6, 100]), 100)

    def test_float(self):
        self.assertEqual(max_integer([10.5, 1.1, 5.1, 12.8]), 12.8)

    def test_zero_number(self):
        self.assertEqual(max_integer([0, 0]), 0)

    def test_big_list(self):
                self.assertEqual(max_integer([100, 200, 300, 400, 620, 222, 901, 666, 767, 882, 999, 245, 879, 998]), 999)

    def test_one_value(self):
        self.assertEqual(max_integer([1]), 1)

    def test_string(self):
        with self.assertRaises(TypeError):
            max_integer(['1', 0])

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(1)

    def tuple_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([(1, 2)], 8)

    def mul_list(self):
        self.assertEqual(max_integer([2, 5 * 5, 6, 1]), 25)

    def loop_in_list(self):
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer([i for i in my_list]), 5)

    def dict_in_list(self):
        with self.assertRaises(TypeError):
            max_length([{"1" : 2,},2])
