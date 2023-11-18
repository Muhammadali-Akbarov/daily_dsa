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
- [Arrays (Lists in Python)](#arrays_in_python)
- [Tuples](#tuples_in_python)
- [Sets](#sets_in_python)
- [Strings](#strings_in_python)
- [Ranges](#range_in_python)
- [Linked Lists](#linked_lists_in_python)

# Methods

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