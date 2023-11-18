Data structure and algorithms are very important for getting a placement as it helps one to solve programming related problems and help us in cracking campus placements in no time.<br>

<img style="width:100%;" src="./static/image.jpg">

# Installation for Python

- 1 - clone repo https://github.com/Muhammadali-Akbarov/daily_dsa.git
- 2 - create a virtual environment and activate
- - `pip3 install virtualenv`
- - `virtualenv env` or `python -m venv env`
- - `env\Scripts\activate (windows)` or `source env/bin/activate (linux)`
- 3 -`cd into project "daily_dsa/python"`
- 4 - `pip install -r requirements.txt`
- 5 - `pylint python`
- 6 - `python tasks/main.py`

Support Group - <a href="https://t.me/+Ng1axYLNyBAyYTRi">Telegram</a> <br/>


## Data Structures

### Built-in Data Structures
- [Arrays (Lists in Python)](#arrays_in_python)
- [Tuples](#tuples_in_python)
- [Sets](#sets_in_python)
- [Dictionaries (hash tables)](#dictionaries_in_python)
- [Strings](#strings_in_python)
- [Ranges](#range_in_python)

### Advanced Data Structures
- [Stacks](#stacks_in_python)
- [Ques](#queues_in_python)
- [Linked Lists](#linked_lists_in_python)
- [Skip Lists (still learning..)](#skip_lists_in_python)


## Algorithms

### Searching
- [LinearSearch](#linear_search_in_python)
- [BinarySearch](#binary_search_in_python)

### Sorting
- [BubbleSort](#bubble_sort_in_python)
- [MergeSort](#merge_sort_in_python)
- [QuickSort](#quick_sort_in_python)
- [SelectSort](#select_sort_in_python)

### Compire searching algorithms
```python
execute in command-line:  python3 python/comparing_searching.py

Total execution time of class name: <function LinearSearch.search at 0x1056defc0> method: search time: 0.0002579689025878906 seconds
Total execution time of class name: <function BinarySearch.search at 0x1056f3920> method: search time: 4.0531158447265625e-06 seconds
```

#### Compare all sort algorithms.
```python
execute in command-line: python3 python/comparing_sorting.py

Total execution time of class name: <function QuickSort.sort at 0x102ed1580> method: sort time: 0.009923696517944336 seconds
Total execution time of class name: <function MergeSort.sort at 0x102e98d60> method: sort time: 0.02179718017578125 seconds
Total execution time of class name: <function SelectionSort.sort at 0x102ed2200> method: sort time: 2.4862358570098877 seconds
Total execution time of class name: <function BubbleSort.sort at 0x102ed1c60> method: sort time: 3.3722269535064697 seconds
```

# Methods

## linear_search_in_python
```python
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
```


## binary_search_in_python
```python
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
```

## arrays_in_python

```python
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
```

## tuples_in_python

```python
"""
tuples in python:
    tuples in python are a versatile and useful data structure
    with several advanced features and use cases,
    here is some advanced information about tuples in python.

immutability tuples are immutable,
    meaning once you create a tuple, you cannot change its elements or size,
    this immutability makes tuples useful for situations
    where you want to ensure that the data remains constant.

features:
    tuple unpacking
    named tuples in collections module.
    slicing
    conversion
    arbitrary nesting
    hashability
"""
import unittest

from collections.abc import namedtuple


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

```

## sets_in_python

```python
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
```

## dictionaries_in_python
```python
""""
dictionaries in python are a versatile and widely used data structure,
here's an advanced overview of python dictionaries:
    internal working:
        hashing:
            when a key-value pair is added to a dictionary,
            python first applies a hash function to the key,
            this hash function computes an integer value (hash) unique to the key (as much as possible),

        index calculation:
            the hash value is then used to calculate an index in an internal array (or hash table),
            this index determines where the key-value pair is stored in the table.

        collision handling:
            sometimes, two different keys may produce the same hash value (a situation known as a collision).
            python handles collisions using a method called "open addressing," which involves probing for the next available
            slot in the hash table.

        dynamic resizing:
            to maintain efficient operations, python dictionaries dynamically resize,
            when the table becomes too crowded (determined by a factor called the load factor),
            python increases the size of the hash table and rehashes all keys to maintain efficiency.

    how works with big O:
        lookup (my_dict.get(key, None)) O(1)
        rehashing O(n)
        deleting O(n)
"""
import unittest


class TestDictionaryMethods(unittest.TestCase):
    """
    test dictionary methods.
    """

    def test_insertion(self) -> None:
        """
        test insertion to dictionary O(1)
        """
        my_dict = {}
        my_dict['name'] = 'Alice'

        self.assertTrue('name' in my_dict)
        self.assertEqual(my_dict['name'], 'Alice')

    def test_lookup(self) -> None:
        """
        test lookup to dictionary
        """
        my_dict = {
            'name': 'Bob',
            'age': 30
        }

        self.assertEqual(my_dict['name'], 'Bob')
        self.assertEqual(my_dict['age'], 30)

        with self.assertRaises(KeyError):
            _ = my_dict['city']

    def test_deletion(self) -> None:
        """
        test the deletion of an existing element.
        """
        my_dict = {
            'name': 'Charlie',
            'age': 25
        }
        del my_dict['name']

        self.assertFalse('name' in my_dict)

        with self.assertRaises(KeyError):
            del my_dict['city']

    def test_iteration(self) -> None:
        """
        test iteration method.
        """
        my_dict = {'name': 'David', 'age': 35}
        keys = []
        values = []

        for key, value in my_dict.items():
            keys.append(key)
            values.append(value)

        self.assertEqual(keys, ['name', 'age'])
        self.assertEqual(values, ['David', 35])

    def test_default_value(self) -> None:
        """
        test the default value.
        """
        my_dict = {
            'name': 'Eve',
            'age': 40
        }
        city = my_dict.get('city', 'Unknown')
        self.assertEqual(city, 'Unknown')

        name = my_dict.get('name', 'Anonymous')
        self.assertEqual(name, 'Eve')


if __name__ == '__main__':
    unittest.main()

```

## strings_in_python

```python
""""
dictionaries in python are a versatile and widely used data structure,
here's an advanced overview of python dictionaries:
    internal working:
        hashing:
            when a key-value pair is added to a dictionary,
            python first applies a hash function to the key,
            this hash function computes an integer value (hash) unique to the key (as much as possible),

        index calculation:
            the hash value is then used to calculate an index in an internal array (or hash table),
            this index determines where the key-value pair is stored in the table.

        collision handling:
            sometimes, two different keys may produce the same hash value (a situation known as a collision).
            python handles collisions using a method called "open addressing," which involves probing for the next available
            slot in the hash table.

        dynamic resizing:
            to maintain efficient operations, python dictionaries dynamically resize,
            when the table becomes too crowded (determined by a factor called the load factor),
            python increases the size of the hash table and rehashes all keys to maintain efficiency.

    how works with big O:
        lookup (my_dict.get(key, None)) O(1)
        rehashing O(n)
        deleting O(n)
"""
import unittest


class TestDictionaryMethods(unittest.TestCase):
    """
    test dictionary methods.
    """

    def test_insertion(self) -> None:
        """
        test insertion to dictionary O(1)
        """
        my_dict = {}
        my_dict['name'] = 'Alice'

        self.assertTrue('name' in my_dict)
        self.assertEqual(my_dict['name'], 'Alice')

    def test_lookup(self) -> None:
        """
        test lookup to dictionary
        """
        my_dict = {
            'name': 'Bob',
            'age': 30
        }

        self.assertEqual(my_dict['name'], 'Bob')
        self.assertEqual(my_dict['age'], 30)

        with self.assertRaises(KeyError):
            _ = my_dict['city']

    def test_deletion(self) -> None:
        """
        test the deletion of an existing element.
        """
        my_dict = {
            'name': 'Charlie',
            'age': 25
        }
        del my_dict['name']

        self.assertFalse('name' in my_dict)

        with self.assertRaises(KeyError):
            del my_dict['city']

    def test_iteration(self) -> None:
        """
        test iteration method.
        """
        my_dict = {'name': 'David', 'age': 35}
        keys = []
        values = []

        for key, value in my_dict.items():
            keys.append(key)
            values.append(value)

        self.assertEqual(keys, ['name', 'age'])
        self.assertEqual(values, ['David', 35])

    def test_default_value(self) -> None:
        """
        test the default value.
        """
        my_dict = {
            'name': 'Eve',
            'age': 40
        }
        city = my_dict.get('city', 'Unknown')
        self.assertEqual(city, 'Unknown')

        name = my_dict.get('name', 'Anonymous')
        self.assertEqual(name, 'Eve')


if __name__ == '__main__':
    unittest.main()

```


## range_in_python
```python
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
```

## stacks_in_python
```python
"""
in python, stacks can be easily implemented using built-in data structures like lists,
a stack is a linear data structure that follows the last in, first out (LIFO) principle,
this means that the last element added to the stack will be the first one to be removed.

basic operations of a stack:
    1) push: add an item to the top of the stack.
    2) pop: remove and return the top item from the stack.
        if the stack is empty, this operation might throw an error or return a special value.

    3) peek or top: Return the top element of the stack without removing it.
    4) is_empty: Check if the stack is empty.
    5) size: Return the number of elements in the stack.

how works with big O:
    1) push: O(1)
    2) pop: O(1)
    3) peek: O(1)
    4) is_empty O(1)
    5) size: O(1)
    6) space complexity: O(n)

use cases:
    stacks are widely used in algorithm implementations,
    function call management (call stack), undo mechanisms in software,
    and for solving certain types of problems (e.g., balanced parenthesis checking, depth-first search in graphs).
"""
import unittest


class Stack:
    """
    the stack class.

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())  # Outputs 3
    print(stack.peek()) # Outputs 2
    print(stack.is_empty()) # Outputs False
    """
    def __init__(self) -> None:
        self.stack = []

    def push(self, item) -> None:
        """
        append an item to the stack.
        """
        self.stack.append(item)

    def pop(self) -> None:
        """
        returns pop element.
        """
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self) -> None:
        """
        returns peek element.
        """
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self) -> None:
        """
        check if stack is empty or not.
        """
        return len(self.stack) == 0

    def size(self) -> None:
        """
        returns size of stack.
        """
        return len(self.stack)


class TestStack(unittest.TestCase):
    """
    test the stack elements.
    """
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        """
        test the push element.
        """
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)

    def test_pop(self):
        """
        test pop.
        """
        self.stack.push(1)
        self.stack.push(2)
        pop_value = self.stack.pop()
        self.assertEqual(pop_value, 2)
        self.assertEqual(self.stack.peek(), 1)

    def test_peek(self):
        """
        test peek.
        """
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)

    def test_is_empty(self):
        """
        test is empty.
        """
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_size(self):
        """
        test size.
        """
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)

    def test_pop_empty_stack(self):
        """
        test pop empty stack.
        """
        self.assertEqual(self.stack.pop(), "Stack is empty")

    def test_peek_empty_stack(self):
        """
        test peek empty stack.
        """
        self.assertEqual(self.stack.peek(), "Stack is empty")


if __name__ == '__main__':
    unittest.main()
```

# queues_in_python
```python
"""
queues are fundamental data structures used in computer science
and programming for managing collections of items in a specific order,
they follow the first-in-first-out (fifo sometimes works as stack (lifo)) principle,
which means that the first item added to the queue is the first one to be removed,
here's some advanced information about queues, including how they work internally.
    internal implementation of queues:
        using lists:
            in python, you can implement a queue using a regular list,
            however, this approach is not very efficient for large queues because
            inserting or removing elements from the beginning of a list (using pop(0) or insert(0, item))
            takes O(n) time complexity due to the need to shift all other elements as a result, it's not
            recommended to large-scale queues.

        queue module:
            python provides a built-in queue module that offers different
            implementations of queues.

        queue operations and big o complexities:
            enqueue (put): adding an item to the end of a queue
            (enqueue operation) typically has an average time complexity of O(1)
            for most queue implementations, in the case of a queue.Queue from the queue module
            , it may involve acquiring and releasing locks, which can introduce some overhead.

        dequeue (delete): removing an item from the front of the queue (dequeue operation) also typically
        has an average time complexity of O(1) for most queue implementations, similar to enqueue,
        thread-safe implementations like queue.Queue may involve acquiring and releasing locks.

        peek: peeking at the front item (without removing) is usually an O(1) operation,
        as it does not require modifying the queue's internal structure.

        use cases for queues:
            task scheduling:
                queues are used in task scheduling systems,
                such as managing tasks in a multithreaded or multiprocessing environment.

            breadth-first search (bfs):
                queues are essential in graph algorithms like bfs,
                where they help explore nodes at different levels in a graph.

            print queue:
                 in operating systems, print jobs are often managed using queues
                 to ensure they are processed in the order they are received.

            message queues:
                in distributed systems, message queues are used for communication between components,
                systems like rabbitmq and apache kafka are popular choices for implementing message queues.

            job queues:
                in web applications, job queues are used to handle asynchronous tasks
                like sending emails or processing background jobs.

            task management:
                queues can be used for managing tasks in various scenarios,
                such as handling customer service requests in a call center
                or processing user actions in a web application.

            queues are versatile data structures with numerous applications
            in computer science and software development, understanding their
            internal workings and complexities is crucial for designing efficient
            systems and algorithms that rely on queues.
"""
import queue
import unittest


class TestQueueMethods(unittest.TestCase):
    """
    test queue methods.
    """
    def test_queue_queue(self) -> None:
        """
        test queue queue method.
        """
        que = queue.Queue()
        que.put(1)
        que.put(2)
        self.assertEqual(que.qsize(), 2)

        item1 = que.get()
        item2 = que.get()
        self.assertEqual(item1, 1)
        self.assertEqual(item2, 2)
        self.assertTrue(que.empty())

    def test_lifo_queue(self) -> None:
        """
        test lifo queue method.
        """
        que = queue.LifoQueue()
        que.put(1)
        que.put(2)
        self.assertEqual(que.qsize(), 2)

        item1 = que.get()
        item2 = que.get()
        self.assertEqual(item1, 2)
        self.assertEqual(item2, 1)
        self.assertTrue(que.empty())

    def test_priority_queue(self) -> None:
        """
        test priority queue.
        """
        pq = queue.PriorityQueue()
        pq.put((3, "high priority"))
        pq.put((1, "highest priority"))
        pq.put((2, "medium priority"))

        item1 = pq.get()
        item2 = pq.get()
        item3 = pq.get()
        self.assertEqual(item1[1], "highest priority")
        self.assertEqual(item2[1], "medium priority")
        self.assertEqual(item3[1], "high priority")
        self.assertTrue(pq.empty())

    def test_simple_queue(self) -> None:
        """
        test the simple queue.
        """
        if hasattr(queue, 'SimpleQueue'):
            q = queue.SimpleQueue()
            q.put(1)
            q.put(2)
            self.assertEqual(q.empty(), False)
            item1 = q.get()
            item2 = q.get()
            self.assertEqual(item1, 1)
            self.assertEqual(item2, 2)
            self.assertEqual(q.empty(), True)


if __name__ == '__main__':
    unittest.main()
```

## linked_lists_in_python
```python
"""
in python, there is no built-in implementation of a linked
list like in some other languages (such as Java or C++),
however, you can create your own linked list structure using classes,
a linked list is a linear data structure where each element is a separate object,
known as a node. Each node contains a reference (or a link) to the next node in the sequence.

    how works with big O:
        insertion:
            O(1) if you insert at the head,
            O(n) if you insert at the tail or in the middle
            (as you need to traverse the list to find the insertion point).

        deletion:
            deletion: O(1) for deleting the head, O(n) for deleting the tail or a middle node.

        search:
            O(n) as you may need to traverse the entire list to find an element.

        use cases:
           linked lists are useful in situations where the number
           of elements is unknown and the memory is to be allocated dynamically,
           they are also used in implementing other data structures like stacks, queues, and graphs.
"""
import unittest


class Node:
    """
    nodes a linked list consists of nodes,
    and each node has two components:
        data: the value or the data held by the node.
        next: a pointer or reference to the next node in the list.

    the first node is called the head of the list,
    and the last node, which points to None, is known as the tail.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.print_list()  # Output: 1 -> 2 -> 3 -> None
    """
    def __init__(self):
        self.head = None

    def append(self, data) -> None:
        """
        appends element to linked list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def get_next(self, data) -> None:
        """
        get next element.
        """
        current = self.head
        while current:
            if current.data == data and current.next:
                return current.next.data
            current = current.next
        return None

    def print_list(self) -> None:
        """
        prints all nodes.
        """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


class DoublyNode:
    """
    double node.
    """
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.print_list()  # Output: 1 <-> 2 <-> 3 <-> None
    """
    def __init__(self) -> None:
        self.head = None

    def append(self, data) -> None:
        """
        appends a new node to the list.
        """
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def get_next(self, data) -> None:
        """
        get next data.
        """
        current = self.head
        while current:
            if current.data == data and current.next:
                return current.next.data
            current = current.next
        return None

    def get_previous(self, data) -> None:
        """
        get previous data
        """
        current = self.head
        while current:
            if current.data == data and current.prev:
                return current.prev.data
            current = current.next
        return None

    def print_list(self) -> None:
        """
        prints element.
        """
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


class CircularLinkedList:
    """
    cll = CircularLinkedList()
    cll.append(1)
    cll.append(2)
    cll.append(3)
    cll.print_list()  # Output: 1 -> 2 -> 3 -> [Head: 1]
    """
    def __init__(self) -> None:
        self.head = None

    def append(self, data) -> None:
        """
        appends data.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def get_next(self, data) -> None:
        """
        get next element.
        """
        current = self.head
        if current is None:
            return None

        start = current
        found = False
        while True:
            if current.data == data:
                found = True
                break
            current = current.next
            if current == start:
                break

        return current.next.data if found else None

    def get_previous(self, data) -> None:
        """
        get previous.
        """
        current = self.head
        if current is None:
            return None

        start = current
        found = False
        while True:
            if current.next.data == data:
                found = True
                break
            current = current.next
            if current == start:
                break

        return current.data if found else None

    def print_list(self) -> None:
        """
        prints lists.
        """
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break

        print(f"[Head: {self.head.data}]")


class TestSinglyLinkedList(unittest.TestCase):
    """
    test singly linked list.
    """
    def setUp(self) -> None:
        self.sll = SinglyLinkedList()
        for i in range(1, 4):
            self.sll.append(i)

    def test_append(self) -> None:
        """
        test append method.
        """
        self.sll.append(4)
        self.assertEqual(self.sll.get_next(3), 4)

    def test_get_next(self) -> None:
        """
        test get next method.
        """
        self.assertIsNone(self.sll.get_next(3))
        self.assertEqual(self.sll.get_next(1), 2)


class TestDoublyLinkedList(unittest.TestCase):
    """
    test doubly linked list.
    """
    def setUp(self) -> None:
        self.dll = DoublyLinkedList()
        for i in range(1, 4):
            self.dll.append(i)

    def test_append(self) -> None:
        """
        test append method.
        """
        self.dll.append(4)
        self.assertEqual(self.dll.get_next(3), 4)
        self.assertEqual(self.dll.get_previous(4), 3)

    def test_get_next_and_previous(self) -> None:
        """
        test get and next and previous.
        """
        self.assertIsNone(self.dll.get_next(3))
        self.assertEqual(self.dll.get_next(1), 2)
        self.assertEqual(self.dll.get_previous(2), 1)
        self.assertIsNone(self.dll.get_previous(1))


if __name__ == '__main__':
    unittest.main()
```

# skip_lists_in_python
```python
"""
skip lists are an advanced data structure that
provide an alternative to balanced trees for implementing
ordered sequences of elements, enabling fast search, insertion,
and deletion operations. They are not a built-in data structure in Python,
but they can be implemented using Python's classes and object-oriented features.

basic concept of a skip list:
    a skip list is made up of layers of linked lists,
    the bottom layer is an ordinary linked list of all the elements,
    each higher layer acts as an "express lane," where nodes skip over several elements,
    allowing faster traversal of the list.

key components of a skip list:
    1) layers: multiple layers of linked lists,
        the bottom layer contains all elements, higher layers allow for faster traversal by skipping nodes.

    2)  nodes: similar to a standard linked list, each node contains data and pointers, in skip lists
        have multiple pointers, one for each level of the list they participate in.

    3) probabilistic balancing:
        instead of rigid balancing rules, skip lists use randomization to determine the levels of each node.

how to skip lists work:

1) search:
    - start from the highest level and traverse the list.
    - if the next node is greater than the search value, move down a level.
    - continue until the bottom level is reached.

2) insertion:
    search for the position where the new element should be inserted
    randomly determine the levels for the new node
    insert the node at each of these levels.

3) deletion:
    search for the node to delete.
    remove the node from each level in which it appears.

how to works with big O:
    search, insertion, deletion:
    1) average case O(log(n))
    2) worst case O(n)

usage and applications:
    skip lists are used in database and file system for indexing.
    they provide a similar alternative to balanced trees.
    they are used in situations where frequent updates are required, and balanced
    tree rotations costly.
"""
import random
import unittest


class Node:
    """
    Node.
    """
    def __init__(self, key, level) -> None:
        self.key = key
        self.forward = [None] * (level + 1)


class SkipList:
    """
    the skip list class.

    skip_list = SkipList(3, 0.5)
    skip_list.insert(3)
    skip_list.insert(6)
    skip_list.insert(7)
    skip_list.insert(9)
    skip_list.insert(12)
    skip_list.insert(19)
    skip_list.insert(17)

    skip_list.display_list()

    print("Search for 19:", skip_list.search(19))
    skip_list.delete(19)
    print("Search for 19 after deletion:", skip_list.search(19))
    skip_list.display_list()

    """
    def __init__(self, max_level, p) -> None:
        self.max_level = max_level
        self.p = p  # Probability for random level generation
        self.header = Node(-1, max_level)
        self.level = 0

    def random_level(self) -> None:
        """
        random level.
        """
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def insert(self, key) -> None:
        """
        the insert method.
        """
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current is None or current.key != key:
            rlevel = self.random_level()

            if rlevel > self.level:
                for i in range(self.level + 1, rlevel + 1):
                    update[i] = self.header
                self.level = rlevel

            new_node = Node(key, rlevel)

            for i in range(rlevel + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def search(self, key) -> None:
        """
        the search method.
        """
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        current = current.forward[0]
        if current and current.key == key:
            return True
        return False

    def delete(self, key) -> None:
        """
        the delete method.
        """
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current is not None and current.key == key:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1

    def display_list(self) -> None:
        """
        display skip lists.
        """
        print("Skip List")
        for lvl in range(self.level + 1):
            print("Level {}: ".format(lvl), end=" ")
            node = self.header.forward[lvl]
            while node is not None:
                print(node.key, end=" ")
                node = node.forward[lvl]
            print("")


class TestSkipList(unittest.TestCase):
    """
    test skip list.
    """
    def setUp(self):
        self.skip_list = SkipList(3, 0.5)
        for i in range(1, 11):
            self.skip_list.insert(i)

    def test_search(self) -> None:
        """
        test search method.
        """
        for i in range(1, 11):
            self.assertTrue(self.skip_list.search(i))
        self.assertFalse(self.skip_list.search(20))

    def test_insert(self) -> None:
        """
        test insert method.
        """
        self.skip_list.insert(12)
        self.assertTrue(self.skip_list.search(12))

    def test_delete(self) -> None:
        """
        test delete method.
        """
        self.skip_list.delete(5)
        self.assertFalse(self.skip_list.search(5))

    def test_random_level(self) -> None:
        """
        test random level.
        """
        level = self.skip_list.random_level()
        self.assertTrue(0 <= level <= self.skip_list.max_level)

    def test_display_list(self) -> None:
        """
        test display list.
        """
        self.skip_list.display_list()


if __name__ == '__main__':
    unittest.main()
```

## bubble_sort_in_python
```python
"""
bubble sort is a simple sorting algorithm that works
by repeatedly stepping through the list to be sorted,
comparing each pair of adjacent items and swapping them if they are in the wrong order,
the pass through the list is repeated until no swaps are needed,
which means the list is sorted, the algorithm gets its name because smaller
elements "bubble" to the top of the list.

how works with big O:
    1) best case: O(n) (when the list already sorted)
    2) average and worst case: O(n^2) (due to nested loops)
    3) space complexity: O(1) (because it's an in-place sorting algorithm)

use cases:
    1) bubble sort is used for educational purposes and in cases where simplicity
    is more important than efficiency, or the list to sort is small.
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
```

## merge_sort_in_python
```python
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
```

## quick_sort_in_python
```python
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
```


## select_sort_in_python
```python
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
```