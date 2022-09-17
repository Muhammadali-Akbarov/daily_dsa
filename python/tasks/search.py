"""
Question:
    Task:
        Massiv ichidan bizga kerakli qiymatning
        indexkini(tartib raqamini) qaytaring.
        Agar qidirilyotgan massiv ichida mavjud bo'lmasa
        -1 yoki None qiymatni qaytaring.
    Example:
     search(myList,11) -> None
    Tools:
        binary search and linear search
    Hint:
        want -> 10
        value -> 1 3 4 6 7 8 10..
        index -> 0 1 2 3 4 5 6..
        answer -> 6
"""
from typing import Any
from typing import List

from unittest import main
from unittest import TestCase


class Searching:
    """Searching object for searching algorithms"""

    @staticmethod
    def linear_search(_list: List[int], want: int) -> int or None:
        """Use this staticmethod for linear search"""

        answer: Any = None
        for index, value in enumerate(_list):
            if value == want:
                answer = index
        return answer

    @staticmethod
    def binary_search(_list: List[int], want: int) -> int or None:
        """Use this staticmethod for binary search"""

        low = 0
        high = len(_list) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = _list[mid]
            if guess == want:
                return mid
            if guess > want:
                high = mid - 1
            else:
                low = mid + 1
        return None


class TestSearching(TestCase):
    """Test for Searching object"""

    def setUp(self) -> None:
        self.search = Searching
        self.list = [1, 3, 4, 6, 7, 8, 10, 12, 23, 45, 56, 78, 99]

    def test_linear_search(self) -> bool:
        """Test for linear search staticmethod"""
        self.assertEqual(6, self.search.linear_search(self.list, 10))
        self.assertEqual(None, self.search.linear_search(self.list, 100))

    def test_binary_search(self) -> bool:
        """Test for binary search staticmethod"""
        self.assertEqual(12, self.search.binary_search(self.list, 99))
        self.assertEqual(None, self.search.binary_search(self.list, 199))


if __name__ == '__main__':
    main()
