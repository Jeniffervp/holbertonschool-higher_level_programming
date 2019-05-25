#!/usr/bin/python3
""" unittest for max integer """

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):

        # test max integer
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertAlmostEqual(max_integer([1.4, 1,7, 8.7], 8.7)
        self.assertAlmostEqual(max_integer([1, 5.6, 3], 5.6)
        self.assertAlmostEqual(max_integer([1.5], 1.5)
        self.assertAlmostEqual(max_integer([-1, -9, -15], -1)
        self.assertAlmostEqual(max_integer([-15], -15)
        self.assertAlmostEqual(max_integer(["Reason","why","The"], why)
        self.assertAlmostEqual(max_integer("Bloody"), y)
        self.assertAlmostEqual(max_integer([], None)
        self.assertAlmostEqual(max_integer(), None)

    def text_error(self):

        # Test errors in max integer
        self.assertRaises(TypeError, max_integer, [1, 'c', 5])
        self.assertRaises(TypeError, max_integer, [3, "hola"])
        self.assertRaises(TypeError, max_integer, [7])
        self.assertRaises(TypeError, max_integer, (1, 5.6, 3))
        self.assertRaises(TypeError, max_integer, (-3))
