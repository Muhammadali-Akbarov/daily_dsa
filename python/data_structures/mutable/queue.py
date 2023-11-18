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
