"""
Question: 1
    Berilgan:
        Uchta sondan eng kattasini
        topish algorithmini toping.

    Formula:
        a,b,c o'zgaruvchilar yaratamiz
        (a and b) < c yoki (a and c) < b yoki (c and b) < a.

    Yechish:
        If condition bilan.

Question 2:
    1 dan N gacha bo'lgan sonlarni
    ko'paytamsini chiqaring.
"""

import math
from unittest import main
from unittest import TestCase


class Numbers:
    """Numbers object"""

    def __init__(self, first: int, second: int, third: int) -> None:
        self.first = first
        self.second = second
        self.third = third

    def find_max(self) -> int:
        """This method finds the maximum value of a given numbers."""
        max_num: int = 0
        if self.first > self.second and self.first > self.third:
            max_num = self.first
        if self.second > self.first and self.second > self.third:
            max_num = self.second
        if self.third > self.second and self.third > self.first:
            max_num = self.third

        return max_num

    def factarial(self):
        """This method multiplies numbers from 1 to N"""
        return math.factorial(self.first)


class TestNumbers(TestCase):
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

    def test_factarial(self) -> int:
        """Checks that the factarial method of Numbers object"""
        self.assertEqual(math.factorial(333), self.obj_first.factarial())
        self.assertEqual(math.factorial(111), self.obj_second.factarial())


if __name__ == '__main__':
    main()
