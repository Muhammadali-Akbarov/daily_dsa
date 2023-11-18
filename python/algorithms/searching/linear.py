"""
linear search, also known as sequential search,
is a straightforward method of searching a list or array,
it works by examining each element of the list in turn until the target element
is found or the end of the list is reached, linear search is a simple and
intuitive search algorithm, often used as an introduction to the concept of
searching in computer science.

basic concepts:
    1) linear search checks each item in the list one by one,
        from the beginning to the end.
    2) it compares each item with the target value to see if they match.
    3) if a match is found, it returns the index of the item,
        or a particular value indicating the position of the found item.

implementation:
    1) it can be implemented using a loop that goes through each element of the list.
    2) if the element is found, the search returns the index of the element,
        if the loop ends without finding the element, the search returns an indication
            that the item was not found (such as -1 or None).

how works with big O:
    1) the time complexity of linear search is O(n), where n is the number of elements in the list.

use cases:
    1) best used when dealing with small lists, or lists that are unsorted and cannot be sorted.
"""
import typing
import unittest

from abstract.searching import Searching

from decorators.excecution import time_execution


class LinearSearch(Searching):
    """
    the implementation of linear search.
    """

    @time_execution
    def search(self, data: typing.List, target: int) -> typing.Union[int, None]:
        """
        the implementation of linear search method.
        """
        for index, value in enumerate(data):
            if value == target:
                return index

        return None


class TestLinearSearch(unittest.TestCase):
    """
    Unit tests for the LinearSearch class.
    """

    def test_search_found(self) -> None:
        """
        Test cases where the target should be found.
        """
        ls = LinearSearch()
        self.assertEqual(ls.search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(ls.search([10, 20, 30, 40, 50], 50), 4)
        self.assertEqual(ls.search([-1, -2, -3, -4, -5], -3), 2)

    def test_search_not_found(self) -> None:
        """
        Test cases where the target should not be found.
        """
        ls = LinearSearch()
        self.assertIsNone(ls.search([1, 2, 3, 4, 5], 6))
        self.assertIsNone(ls.search([10, 20, 30, 40, 50], 60))
        self.assertIsNone(ls.search([-1, -2, -3, -4, -5], 0))

    def test_empty_list(self) -> None:
        """
        Test cases with an empty list.
        """
        ls = LinearSearch()
        self.assertIsNone(ls.search([], 1))


if __name__ == '__main__':
    unittest.main()
