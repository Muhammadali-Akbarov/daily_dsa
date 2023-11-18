"""
The range type in Python is an immutable sequence of numbers and is commonly used for
looping a specific number of times in for loops. It's not just a list of numbers but rather a more
memory-efficient way to represent a range of numbers because it stores only the start, stop, and step values,
computing individual items and subranges as needed.

    memory efficiency:
        unlike a list, range doesn't store all the values in memory,
        tt generates the numbers on-the-fly as you iterate over it.

    immutable:
        once a range object is created,
        it cannot be altered. Its start, stop, and step values are fixed.

    slicing:
        you can slice range objects similar to lists,
        but the result will also be a range object, not a list.

    indexing:
        supports positive and negative indexing to access elements.
"""

import unittest


class TestListOperations(unittest.TestCase):
    """
    test list operations.
    """
    def setUp(self):
        self.test_list = [1, 2, 3, 4, 5]

    def test_list_append(self) -> None:
        """
        test list append.
        """
        self.test_list.append(6)
        self.assertEqual(self.test_list, [1, 2, 3, 4, 5, 6])

    def test_list_access_by_index(self) -> None:
        """
        test list access by index
        """
        element = self.test_list[2]
        self.assertEqual(element, 3)

    def test_list_insert(self) -> None:
        """
        test list insert
        """
        self.test_list.insert(2, 'inserted')
        self.assertEqual(self.test_list, [1, 2, 'inserted', 3, 4, 5])


class TestDictionaryOperations(unittest.TestCase):
    """
    test dictionary operations.
    """
    def setUp(self):
        self.test_dict = {'a': 1, 'b': 2, 'c': 3}

    def test_dict_access(self) -> None:
        """
        test dict access
        """
        value = self.test_dict['b']
        self.assertEqual(value, 2)

    def test_dict_insert(self) -> None:
        """
        test dict insert
        """
        self.test_dict['d'] = 4
        self.assertEqual(self.test_dict['d'], 4)

    def test_dict_delete(self) -> None:
        """
        test dict delete
        """
        del self.test_dict['c']
        self.assertNotIn('c', self.test_dict)


if __name__ == '__main__':
    unittest.main()
