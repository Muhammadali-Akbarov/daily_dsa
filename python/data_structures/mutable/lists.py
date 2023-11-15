"""
arrays:
    in computer science, an array is a fixed-size,
    ordered collection of elements of the same data type,
    arrays have a fixed length, meaning that once you create
    an array with a specific size, you cannot change
    its size without creating a new array.

arrays in python:
    arrays in python are implemented as dynamic arrays,
    which means that their size can grow or shrink dynamically as elements
    are added or removed, python's built-in array module provides a way to
    create arrays of a specific data type, but most often, when people refer
    to "arrays" in Python, they are actually referring to "lists."

lists in python:
    in python, a list is a dynamic array that can contain elements of
    different data types, and it is one of the most commonly used data
    structures. lists are implemented as dynamic arrays,
    meaning that they can change in size as needed, lists are ordered collections of elements,
    they can contain elements of different data types and are mutable (modifiable).

how works with big O:
    big O notation is a way to describe the performance characteristics
    of algorithms or data structures, including lists (arrays or dynamic arrays),
    by analyzing how their performance scales with the size of the input data,
    when analyzing lists, you're typically concerned with operations like access,
    insertion, and deletion. here's how big O principles apply to lists:

    access (read/write) - O(1):
        in dynamic arrays (python lists),
        accessing elements by index is typically an O(1) operation,
        this means that regardless of the size of the list,
        the time it takes to access an element at a specific index remains constant.
        this is because dynamic arrays use contiguous memory locations,
        and simple arithmetic is used to calculate the memory address of the desired element.

    insertion at the end - O(1) (amortized):
        inserting an element at the end of a dynamic array is usually an O(1) operation on average,
        but it can become O(n) in some cases when the underlying array needs to be resized,
        however, dynamic arrays typically use amortization to minimize the frequency of resizing,
        making the average insertion at the end O(1).

    insertion at the beginning - O(n):
        inserting an element at the beginning of a dynamic array requires
        shifting all existing elements to make room for the new element,
        this operation is O(n), where n is the number of elements in the array,
        as it involves copying all elements to new memory locations.

    deletion - O(n):
        deleting an element in a dynamic array, except at the end,
        also requires shifting elements to close the gap created by the removal,
        this operation is O(n), similar to insertion at the beginning,
        because it involves copying elements.

    search - O(n):
        searching for an element in an unsorted dynamic array typically requires iterating through
        the array until the element is found or reaching the end. This is an O(n) operation because,
        in the worst case, you may need to examine all elements.
"""
import time
import unittest


class TestListInsertion(unittest.TestCase):
    """
    test list insertion.
    """
    def test_insert_element(self) -> None:
        """
        test insert element to list.
        if we want to insert an element in the list
        processor will execute shift operations.
        if my case shift operations will be executed 11 times (O(n)
        inserting an element at the beginning of a dynamic array)
        and insert operation will be executed 1 time.
        """
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        start_time = time.time_ns()

        my_list.insert(0, 12)

        end_time = time.time_ns()

        elapsed_time = end_time - start_time

        self.assertIn(
            member=12,
            container=my_list,
            msg="inserted element should be in the list"
        )

        self.assertEqual(
            first=len(my_list),
            second=12,
            msg="list length should increase by 1"
        )

        self.assertGreater(
            a=elapsed_time,
            b=-1,
            msg="elapsed time should be positive"
        )


if __name__ == '__main__':
    unittest.main()
