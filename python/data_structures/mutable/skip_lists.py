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
