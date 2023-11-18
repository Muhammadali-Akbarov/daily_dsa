"""
Question: 1
    Task:
        Find a maximum value from given lists.

    Example:
        a,b,c define variables
        (a and b) < c or (a and c) < b or (c and b) < a.

    Tools:
        If condition.
"""
import unittest


class Numbers:
    """
    Numbers object
    """
    def __init__(self, first: int, second: int, third: int) -> None:
        self.first = first
        self.second = second
        self.third = third

    def find_max(self) -> int:
        """
        This method finds the maximum value of a given numbers.
        """
        max_num: int = 0
        if self.first > self.second and self.first > self.third:
            max_num = self.first
        if self.second > self.first and self.second > self.third:
            max_num = self.second
        if self.third > self.second and self.third > self.first:
            max_num = self.third

        return max_num


class TestNumbers(unittest.TestCase):
    """Test for Numbers object"""
    def setUp(self) -> None:
        self.obj_first = Numbers(333, 222, 111)
        self.obj_second = Numbers(111, 333, 222)
        self.obj_third = Numbers(111, 222, 333)

    def test_find_max(self) -> None:
        """Checks that the find_max method of Numbers object"""
        self.assertEqual(333, self.obj_first.find_max())
        self.assertEqual(333, self.obj_second.find_max())
        self.assertEqual(333, self.obj_third.find_max())


if __name__ == '__main__':
    unittest.main()
