"""
divide and conquer

how to works big big O:
    1) best and average case: O(n log(n))
    2) worst case: O(n^2) (but this is rare with good pivot choice)

use cases:
    quicksort is best used when average-case performance is important and additional
    space for merges is not available, it's a common choice for internal sorting
    in many standard libraries due to its practical efficiency.
"""
import unittest

from typing import List

from abstract.sorting import Sorting

from decorators.excecution import time_execution


class QuickSort(Sorting):
    """
    the sorting class.
    """
    @time_execution
    def sort(self, data: List):
        """
        quick sort method.
        """
        if len(data) <= 1:
            return data

        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]

        return self.sort(left) + middle + self.sort(right)


class TestQuickSort(unittest.TestCase):
    """
    quick sort test cases.
    """
    def setUp(self):
        self.sorting = QuickSort()

    def test_empty_list(self):
        """
        test the empty list method.
        """
        empty_list = []

        self.assertEqual(
            self.sorting.quick_sort(empty_list),
            empty_list
        )

    def test_single_element(self):
        """
        test the single element.
        """
        single_element = [1]

        self.assertEqual(
            self.sorting.quick_sort(single_element),
            single_element
        )

    def test_sorted_list(self):
        """
        test sorted list.
        """
        sorted_list = [1, 2, 3, 4, 5]

        self.assertEqual(
            self.sorting.quick_sort(sorted_list),
            [1, 2, 3, 4, 5]
        )

    def test_reverse_sorted_list(self):
        """
        test reverse sorted list.
        """
        unsorted_list = [5, 4, 3, 2, 1]
        sorted_list = [1, 2, 3, 4, 5]

        self.assertEqual(
            self.sorting.quick_sort(unsorted_list),
            sorted_list
        )

    def test_unsorted_list(self):
        """
        test unsorted list.
        """
        unsorted_list = [3, 6, 1, 8, 4, 5]
        sorted_list = [1, 3, 4, 5, 6, 8]

        self.assertEqual(
            self.sorting.quick_sort(unsorted_list),
            sorted_list
        )

    def test_duplicate_elements(self):
        """
        test duplicate elements.
        """
        dublicate_list = [3, 6, 1, 3, 4, 5]
        sorted_list = [1, 3, 3, 4, 5, 6]

        self.assertEqual(
            self.sorting.quick_sort(dublicate_list),
            sorted_list
        )


if __name__ == '__main__':
    unittest.main()
