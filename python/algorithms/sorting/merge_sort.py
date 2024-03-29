"""
merge sort is an efficient, stable, comparison-based,
divide and conquer sorting algorithm, it divides the input array into two halves,
calls itself for the two halves, and then merges the two sorted halves,
the merge step is the key operation of the algorithm,
here’s a detailed explanation of how merge sort works in Python:

divide and conquer:
    - the list is divided into two (or more) sub lists,
    repeatedly, until each sublist has only one element (which is inherently sorted)
    - this dividing step is a straightforward process of splitting the list into halves.

how to works with big O:
    1) best average and worst case: O((n)log(n))
    2) O(n) the algorithm requires additional space for temporary arrays
        used during the merge process.
"""
import unittest

from typing import List

from abstract.sorting import Sorting

from decorators.excecution import time_execution


class MergeSort(Sorting):
    """
    the sorting class
    """
    @time_execution
    def sort(self, data: List):
        """
        the merge sort method.
        """
        if len(data) > 1:
            mid = len(data) // 2  # Finding the mid of the array
            left = data[:mid]  # Dividing the array elements into 2 halves
            right = data[mid:]

            self.sort(left)  # Sorting the first half
            self.sort(right)  # Sorting the second half

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    data[k] = left[i]
                    i += 1
                else:
                    data[k] = right[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(left):
                data[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                data[k] = right[j]
                j += 1
                k += 1


class TestMergeSort(unittest.TestCase):
    """
    the test merge sort class.
    """
    def test_merge_sort(self):
        """
        test merge sort method.
        """
        sort_obj = MergeSort()
        test_cases = [
            ([], []),
            ([1], [1]),
            ([3, 2, 1], [1, 2, 3]),
            ([5, 3, 8, 6, 7, 2], [2, 3, 5, 6, 7, 8]),
            ([10, -1, 2, 11, 5], [-1, 2, 5, 10, 11])
        ]

        for test_input, expected_output in test_cases:
            with self.subTest(
                test_input=test_input,
                expected_output=expected_output
            ):
                sort_obj.sort(test_input)
                self.assertEqual(test_input, expected_output)


if __name__ == '__main__':
    unittest.main()
