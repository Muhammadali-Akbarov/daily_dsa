"""
Question:
    Find a factorial for given number.
"""
import math

import unittest


class Factorial:
    """
    the factorial class
    """
    @staticmethod
    def find(number: int) -> int:
        """
        find the factorial for given number.
        """
        return math.factorial(number)


class FactorialTestCase(unittest.TestCase):
    """
    the factorial class's test cases.
    """
    def setUp(self):
        """
        setting-up the factorial class
        """
        self.factorial = Factorial()

    def test_find_factorial_(self):
        """
        test find_factorial method.
        """
        self.assertEqual(120, self.factorial.find(
            number=5
        ))
        self.assertEqual(720, self.factorial.find(
            number=6
        ))
        self.assertEqual(3628800, self.factorial.find(
            number=10
        ))


if __name__ == '__main__':
    unittest.main()
