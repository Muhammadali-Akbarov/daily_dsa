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
