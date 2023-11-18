"""
binary search is an efficient algorithm for finding
an item from a sorted list of items, it works by repeatedly dividing
in half the portion of the list that could contain the item, until you've narrowed down
the possible locations to just one.

basic concepts:
    1) divide and conquer:
        binary search starts by comparing the middle item of the list with the target value.
    2) if the target value matches the middle item, the search is complete.
    3) if the target value is less than the middle item, the search continues on the left half of the list,
        otherwise, it continues on the right half.

efficient searching:
    by dividing the list in half with each step, binary search
    reduces the number of comparisons drastically compared to linear search.

requirement of sorted list:
    binary search can only be applied to a list that is already sorted.

how works with big O principles:
    1) the time complexity of binary search is O(log(n)),
        where n is the number of elements in the list.
    2) this logarithmic complexity is much more efficient then linear search O(n),
        especially for large lists.
"""

import typing
import unittest

from abstract.searching import Searching

from decorators.excecution import time_execution


class BinarySearch(Searching):
    """
    The implementation of binary search.
    """

    @time_execution
    def search(self, data: typing.List, target: int) -> typing.Union[int, None]:
        """
        The implementation of binary search method.
        """
        left, right = 0, len(data) - 1
        while left <= right:
            mid = (left + right) // 2
            if data[mid] == target:
                return mid
            elif data[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return None


class TestBinarySearch(unittest.TestCase):
    """
    Unit tests for the BinarySearch class.
    """

    def test_search_found(self) -> None:
        """
        Test cases where the target should be found.
        """
        bs = BinarySearch()
        self.assertEqual(bs.search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(bs.search([10, 20, 30, 40, 50], 50), 4)
        self.assertEqual(bs.search([-5, -4, -3, -2, -1], -3), 2)

    def test_search_not_found(self) -> None:
        """
        Test cases where the target should not be found.
        """
        bs = BinarySearch()
        self.assertIsNone(bs.search([1, 2, 3, 4, 5], 6))
        self.assertIsNone(bs.search([10, 20, 30, 40, 50], 60))
        self.assertIsNone(bs.search([-5, -4, -3, -2, -1], 0))

    def test_empty_list(self) -> None:
        """
        Test cases with an empty list.
        """
        bs = BinarySearch()
        self.assertIsNone(bs.search([], 1))


if __name__ == "__main__":
    unittest.main()
