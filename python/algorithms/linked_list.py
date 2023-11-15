"""
linked list examples
"""
import unittest

from typing import Any
from typing import Union


class Node:
    """
    node object.
    """
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Union[Node, None] = None


class LinkedList:
    """
    linked list examples.
    """
    def __init__(self):
        self.head: Union[Node, None] = None

    def print_list(self) -> None:
        """
        show list of linked lists.
        """
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def add_new_node(self, new_data: str) -> None:
        """
        add a new node.
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    @staticmethod
    def insert_after(prev_node: Node, new_node: str) -> None:
        """
        insert after a node.
        """
        if prev_node is None:
            print("No previous node")
            return

        new_node = Node(new_node)
        new_node.next = prev_node.next
        prev_node.next = new_node


class TestLinkedList(unittest.TestCase):
    """
    the linked list test case
    """
    def setUp(self):
        """
        setting-up linked list class
        """
        self.linked_list = LinkedList()

    def test_add_new_node(self):
        """
        test a new node method
        """
        self.linked_list.add_new_node('Monday')
        self.assertIsNotNone(self.linked_list.head)
        self.assertEqual(self.linked_list.head.data, 'Monday')

    def test_insert_after(self):
        """
        test a new insert after method.
        """
        self.linked_list.add_new_node('Monday')
        self.linked_list.add_new_node('Tuesday')

        # Inserting 'Wednesday' after 'Monday'
        self.linked_list.insert_after(self.linked_list.head.next, 'Wednesday')

        second_node = self.linked_list.head.next
        third_node = second_node.next if second_node else None

        self.assertIsNotNone(third_node)
        self.assertEqual(third_node.data, 'Wednesday')

    def test_linked_list_structure(self):
        """
        test linked list structure.
        """
        self.linked_list.add_new_node('Monday')
        self.linked_list.add_new_node('Tuesday')
        self.linked_list.add_new_node('Wednesday')

        first_data = self.linked_list.head.data \
            if self.linked_list.head else None
        second_data = self.linked_list.head.next.data \
            if self.linked_list.head.next else None
        third_data = self.linked_list.head.next.next.data \
            if self.linked_list.head.next.next else None

        self.assertEqual(first_data, 'Wednesday')
        self.assertEqual(second_data, 'Tuesday')
        self.assertEqual(third_data, 'Monday')


if __name__ == '__main__':
    unittest.main()
