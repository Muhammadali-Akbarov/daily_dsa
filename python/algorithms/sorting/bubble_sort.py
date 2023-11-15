"""
bubble sort
"""
import unittest
from typing import List

from abstract.sorting import Sorting

from decorators.excecution import time_execution


class BubbleSort(Sorting):
    """
    the bubble sort class.
    """
    @staticmethod
    @time_execution
    def sort(data: List) -> List:
        """
        bubble sort method.
        """
        lenth = len(data)
        for i in range(lenth):
            for j in range(0, lenth-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]

        return data


class TestBubbleSort(unittest.TestCase):
    """
    the test bubble sort class.
    """
    def setUp(self):
        """
        setting-up the test bubble sort class.
        """
        self.sorting = BubbleSort()

    def test_empty_list(self):
        """
        test the empty list method
        """
        arr = []
        self.assertEqual(self.sorting.bubble_sort(arr), [])

    def test_sorted_list(self):
        """
        test the sorted list method
        """
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(self.sorting.bubble_sort(arr), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        """
        test the reverse sorted list method.
        """
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(self.sorting.bubble_sort(arr), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        """
        test the unsorted list method.
        """
        arr = [3, 6, 1, 8, 4, 5]
        self.assertEqual(self.sorting.bubble_sort(arr), [1, 3, 4, 5, 6, 8])

    def test_duplicate_elements(self):
        """
        test the dublicate elements method.
        """
        arr = [3, 6, 1, 3, 4, 5]
        self.assertEqual(self.sorting.bubble_sort(arr), [1, 3, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
