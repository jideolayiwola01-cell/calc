# test_calc.py
import unittest
from calk import remove_zero_decimal


class TestCalc(unittest.TestCase):

    def test_removes_decimal_from_whole_number(self):
        self.assertEqual(remove_zero_decimal(4.0), "4")

    def test_keeps_decimal_for_float(self):
        self.assertEqual(remove_zero_decimal(4.5), "4.5")

    def test_negative_whole_number(self):
        self.assertEqual(remove_zero_decimal(-3.0), "-3")

    def test_zero(self):
        self.assertEqual(remove_zero_decimal(0.0), "0")


if __name__ == "__main__":
    unittest.main()
