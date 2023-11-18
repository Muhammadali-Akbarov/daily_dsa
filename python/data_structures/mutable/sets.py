"""
sets in python are a fundamental data structure that
represents an unordered collection of unique elements,
here's more information about sets in python:

features:
    uniqueness:
        sets automatically remove duplicate elements,
        storing only unique items.

    unordered:
        the elements in a set are not stored in any particular order,
        meaning they don't support indexing or slicing.

    mutability:
        standard sets are mutable, meaning elements can be added or removed,
        python also offers an immutable version called frozenset.

    set comprehensions:
        python supports set comprehensions,
        a concise way to create sets based on existing iterables

how works with big O:
    creation (set(iterable)):
        time complexity: O(n) - proportional to the number of elements in the iterable.

    insertion (set.add(elem)):
        time complexity: O(1) - generally constant time,
        although can be worse if a rehash is required.

    deletion set.remove(elem), set.discard(elem):
        time Complexity: O(1) - typically constant time,
        but can vary depending on the structure of the
        set and the element being removed.

    membership test (elem in set):
        time complexity: O(1) - usually constant time due to hashing,
        but can degrade in certain cases.

    length calculation (len(set)):
        time Complexity: O(1) - constant time operation.

    set operations involving two sets:
        union (set1 | set2 or set1.union(set2))
        time complexity: O(n + m) - where n and m are the sizes of the sets.

    intersection (set1 & set2 or set1.intersection(set2)):
        time complexity: O(min(n, m)) - where n and m are the sizes of the sets
        iterates over the smaller set and checks for membership in the larger set.

    difference (set1 - set2 or set1.difference(set2)):
        time complexity: O(n) - where n is the size of the set1;
        iterates over set1 and checks for non-membership in set2.

    symmetric Difference (set1 ^ set2 or set1.symmetric_difference(set2))
        time Complexity: O(n + m) - involves iterating over both sets.
"""
import unittest


class TestSetOperations(unittest.TestCase):
    """
    the testcases for set operations
    """
    def setUp(self):
        # This method is called before each test
        self.set1 = {1, 2, 3}
        self.set2 = {3, 4, 5}

    def test_union(self) -> None:
        """
        the test union.
        """
        result = self.set1 | self.set2
        self.assertEqual(result, {1, 2, 3, 4, 5})

    def test_intersection(self) -> None:
        """
        the test intersection.
        """
        result = self.set1 & self.set2
        self.assertEqual(result, {3})

    def test_difference(self) -> None:
        """
        the test differance
        """
        result = self.set1 - self.set2
        self.assertEqual(result, {1, 2})

    def test_symmetric_difference(self) -> None:
        """
        the test symmetric differance
        """
        result = self.set1 ^ self.set2
        self.assertEqual(result, {1, 2, 4, 5})

    def test_subset(self) -> None:
        """
        the test subset.
        """
        self.assertTrue({1, 2}.issubset(self.set1))

    def test_superset(self) -> None:
        """
        the test superset.
        """
        self.assertTrue(self.set1.issuperset({1, 2}))

    def test_membership(self) -> None:
        """
        the test membership.
        """
        self.assertIn(1, self.set1)
        self.assertNotIn(4, self.set1)

    def test_add_and_remove(self) -> None:
        """
        the test add and remove.
        """
        self.set1.add(4)
        self.assertIn(4, self.set1)
        self.set1.remove(4)
        self.assertNotIn(4, self.set1)

    def test_discard(self) -> None:
        """
        the test discard.
        """
        self.set1.discard(3)
        self.assertNotIn(3, self.set1)

    def test_len(self) -> None:
        """
        the test len.
        """
        self.assertEqual(len(self.set1), 3)

    def test_copy(self) -> None:
        """
        the test copy.
        """
        set_copy = self.set1.copy()
        self.assertEqual(set_copy, self.set1)

    def test_clear(self) -> None:
        """
        the test clear
        """
        self.set1.clear()
        self.assertEqual(len(self.set1), 0)


if __name__ == '__main__':
    unittest.main()
