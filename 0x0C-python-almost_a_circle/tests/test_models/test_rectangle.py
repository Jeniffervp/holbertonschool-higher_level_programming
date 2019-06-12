#!/usr/bin/python3
""" Module to test rectangle """
import unittest
import pep8
from models.rectangle import Rectangle


class format_pep8(unittest.TestCase):
    """Class to test pep8 """
    def test_pep8_rec(self):
        """ Function to test pep8 """
        checker = pep8.Checker("models/rectangle.py", show_source=True)
        file_error= checker.check_all()

class Test_Rectangle_work(unittest.TestCase):
    """Class to test the Rectangle """

    def setUp(self):
        """ function to set variables"""
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)

    def tearDown(self):
        """ function to restart a process """
        pass

    def test_id(self):
        """Function to test the id cases """
        self.assertEqual(self.r1.id, 35)
        self.assertEqual(self.r2.id, 36)
        self.assertEqual(self.r3.id, 12)

    def test_width(self):
        """funtion to test width case """
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 10)

    def test_height(self):
        """ Function to test height cases """
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r3.height, 2)

    def test_x(self):
        """ function to test the x case """
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r3.x, 0)


    def test_y(self):
        """ function to test y case """
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 0)

if __name__ == "__main__":
    unittest.main()
