"""
recursion usage.
"""
import math
import unittest


class Recursion:
    """
    recursion object for recursion usages.
    """

    def decount(self, number: int) -> int or None:
        """
        decount recursion.
        """
        result: int = None
        print("number", number)

        if not (number == 0 or not number):
            result = self.decount(number-1)

        return result

    def factorial(self, number: int) -> int or None:
        """
        factorial recursion.
        """
        result: int = None

        if not (number == 0 or not number):
            result = math.factorial(number)

        return result


class RecursionTestCase(unittest.TestCase):
    """
    Recursion test for recursion usages.
    """

    def setUp(self) -> None:
        """
        Setting up recursion.
        """
        self.recursion = Recursion()

    def test_decount(self):
        """
        test decount recursion.
        """
        self.assertEqual(
            self.recursion.decount(5), None, "Should return None"
        )
        self.assertEqual(
            self.recursion.decount(0), None, "Should return None"
        )

    def test_factorial(self):
        """
        test factorial recursion.
        """
        self.assertEqual(
            self.recursion.factorial(5), 120, "Should return 120"
        )
        self.assertEqual(
            self.recursion.factorial(0), None, "Should return None"
        )
        self.assertEqual(
            self.recursion.factorial(1), None, "Should return None"
        )


if __name__ == "__main__":
    unittest.main()
