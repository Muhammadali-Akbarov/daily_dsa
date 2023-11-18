"""
selection sort creates a new empty array
and compares gives array's elements and sorts to new array.

how to works with big O:
    time complexity: best, average and worst case: O(n^2), this is because
        of the two nested loops, each running N times in the worst case.

    space complexity:
        O(1). the algorithm only uses a constant amount of additional memory space, making it an in-place sorting algorithm.
"""
import unittest
from typing import List

from abstract.sorting import Sorting
from decorators.excecution import time_execution


class SelectionSort(Sorting):
    """
    selection sort class
    """
    @staticmethod
    @time_execution
    def sort(data: List):
        """
        selection sort, BIG O n*n
        """
        for i, _ in enumerate(data):
            min_index = i
            for j in range(i+1, len(data)):
                if data[min_index] > data[j]:
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]

        return data


class SelectionSortTestCase(unittest.TestCase):
    """
    the selection test cases.
    """
    def setUp(self) -> None:
        """
        setting up the test case.
        """
        self.selection_sort = SelectionSort()

    def test_selection_sort(self):
        """
        test selection sort for given array
        """
        unsorted_list = [64, 25, 12, 22, 11]
        sorted_list = [11, 12, 22, 25, 64]

        self.assertEqual(sorted_list, self.selection_sort.selection_sort(
            arr=unsorted_list
        ))


if __name__ == '__main__':
    unittest.main()
