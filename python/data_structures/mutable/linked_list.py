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
