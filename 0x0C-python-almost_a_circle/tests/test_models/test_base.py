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

    def test_base_normal(self):
        """Function to test the predefined cases """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_0(self):
        """funtion to test zero case """
        b6 = Base(0)
        self.assertEqual(b6.id, 0)

    def test_neg(self):
        """Function to test negative cases """
        b7 = Base(-2)
        self.assertEqual(b7.id, -2)

    def test_float(self):
        """function to test the float cases """
        b8 = Base(2.5)
        self.assertEqual(b8.id, 2.5)

    def test_str(self):
        """function to test string """
        b9 = Base("Gummy")
        self.assertEqual(b9.id, "Gummy")

    def test_list(self):
        """function to test list case """
        b10 = Base([1, 2, 3])
        self.assertEqual(b10.id, [1, 2, 3])

    def test_tup(self):
        """function to test tuples case """
        b11 = Base((1, 2, 3))
        self.assertEqual(b11.id, (1, 2, 3))

    def test_dict(self):
        """function to test dictionary """
        b12 = Base({'a': 1, 'b': 2})
        self.assertEqual(b12.id, {'a': 1, 'b': 2})

if __name__ == "__main__":
    unittest.main()
