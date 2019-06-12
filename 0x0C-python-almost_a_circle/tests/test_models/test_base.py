#!/usr/bin/python3
import unittest
import pep8
from models.base import Base


class format_pep8(unittest.TestCase):
    """Class to test pep8 """
    def test_pep8(self):
        """ Function to test pep8 """
        checker = pep8.Checker("models/base.py", show_source=True)
        file_error= checker.check_all()

class Test_Base_work(unittest.TestCase):
    """Class to test the base """

    def setUp(self):
        """ function to set variables"""
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()

    def tearDown(self):
        """ function to restart a process """
        pass

    def test_id(self):
        """Function to test the predefined cases """
        self.assertEqual(self.b1.id, 13)
        self.assertEqual(self.b2.id, 14)
        self.assertEqual(self.b3.id, 15)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 16)

    def test_0(self):
        """funtion to test zero case """
        self.b1 = Base(0)
        self.assertEqual(self.b1.id, 0)

    def test_neg(self):
        """Function to test negative cases """
        self.b1 = Base(-2)
        self.assertEqual(self.b1.id, -2)

    def test_float(self):
        """function to test the float cases """
        self.b1 = Base(2.5)
        self.assertEqual(self.b1.id, 2.5)

    def test_str(self):
        """function to test string """
        self.b1 = Base("Gummy")
        self.assertEqual(self.b1.id, "Gummy")

    def test_list(self):
        """function to test list case """
        self.b1 = Base([1, 2, 3])
        self.assertEqual(self.b1.id, [1, 2, 3])

    def test_tup(self):
        """function to test tuples case """
        self.b1 = Base((1, 2, 3))
        self.assertEqual(self.b1.id, (1, 2, 3))

    def test_dict(self):
        """function to test dictionary """
        self.b1 = Base({'a': 1, 'b': 2})
        self.assertEqual(self.b1.id, {'a': 1, 'b': 2})

if __name__ == "__main__":
    unittest.main()
