"""
tuples in python:
    tuples in python are a versatile and useful data structure
    with several advanced features and use cases,
    here is some advanced information about tuples in python.

immutability tuples are immutable:
    meaning once you create a tuple, you cannot change its elements or size,
    this immutability makes tuples useful for situations
    where you want to ensure that the data remains constant.

features:
    tuple unpacking:
        you can easily unpack the elements of a tuple into separate variables.
        this is commonly used when working with functions that return multiple values.

    named tuples in collections module:
        the collections module provides a namedtuple factory function,
        which creates named tuples with named fields,
        named tuples are similar to regular tuples but allow you to access elements by name,
        making your code more readable.

    slicing:
        you can slice tuples to create new tuples or extract specific subsets of elements,
        tuple slicing follows the same syntax as list slicing.

    conversion:
        you can convert other iterable objects,
        such as lists or strings, into tuples using the tuple() constructor.

    arbitrary nesting:
        tuples can be nested within each other to create complex data structures,
        this nesting allows you to represent hierarchical or structured data.

    hashability:
        tuples are hashable and can be used as keys in dictionaries,
        unlike lists which are mutable and cannot be used as dictionary keys.
"""
import unittest

from collections import namedtuple


class TestTuples(unittest.TestCase):
    """
    test the tuple features.
    """
    def test_tuple_unpacking(self) -> None:
        """
        test unpacking feature.
        """
        my_tuple = (1, 2, 3)

        a, b, c = my_tuple
        self.assertEqual(a, 1)
        self.assertEqual(b, 2)
        self.assertEqual(c, 3)

    def test_named_tuples(self) -> None:
        """
        test named tuples.
        """
        Point = namedtuple("Point", ["x", "y"])
        p = Point(3, 4)

        self.assertEqual(p.x, 3)
        self.assertEqual(p.y, 4)

    def test_slicing(self) -> None:
        """
        test slicing feature.
        """
        my_tuple = (1, 2, 3, 4, 5)

        subset = my_tuple[1:4]
        self.assertEqual(subset, (2, 3, 4))

    def test_conversion(self) -> None:
        """
        test conversion feature.
        """
        my_list = [1, 2, 3]

        my_tuple = tuple(my_list)
        self.assertEqual(my_tuple, (1, 2, 3))

    def test_arbitrary_nesting(self) -> None:
        """
        test arbitrary nesting feature.
        """
        nested_tuple = (1, (2, 3), (4, 5, (6, 7)))

        self.assertEqual(nested_tuple[1][0], 2)
        self.assertEqual(nested_tuple[2][2][1], 7)

    def test_hashability(self) -> None:
        """
        test hashability
        """
        my_dict = {(1, 2): "value"}

        self.assertEqual(my_dict[(1, 2)], "value")


if __name__ == '__main__':
    unittest.main()
