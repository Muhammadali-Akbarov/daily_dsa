"""
the stack is LIFO data struct
Last in First Out. (mail-messages, calling-history, etc.)
that includes push, pop, is_empty, is_full, peek methods.
"""
import typing
import unittest


class Stack:
    """
    the stack class.
    """
    def __init__(self) -> None:
        self.items = []

    def is_empty(self) -> bool:
        """
        check if the stack is empty or not.
        """
        return not self.items

    def push(self, item) -> None:
        """
        add a new item to the stack.
        """
        self.items.append(item)

    def pop(self) -> typing.Any:
        """
        gets and removes the item from the stack.
        """
        result: typing.Any = None

        if not self.is_empty():
            result = self.items.pop()

        return result

    def peek(self):
        """
        returns peek of element from the stack.
        """
        result: typing.Any = None

        if not self.is_empty():
            result = self.items[-1]

        return result

    def size(self):
        """
        returns size of element from the stack.
        """
        return len(self.items)


class TestStack(unittest.TestCase):
    """
    Test Stock class
    """
    def setUp(self):
        """
        setting-up stack class.
        """
        self.stack = Stack()

    def test_is_empty(self):
        """
        test the is_empty method.
        """
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_push(self):
        """
        test the push method.
        """
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)

    def test_pop(self):
        """
        test the pop method.
        """
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertIsNone(self.stack.pop())

    def test_peek(self):
        """
        test the peek method.
        """
        self.assertIsNone(self.stack.peek())
        self.stack.push(4)
        self.assertEqual(self.stack.peek(), 4)
        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5)

    def test_size(self):
        """
        test the size method.
        """
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)


if __name__ == '__main__':
    unittest.main()
