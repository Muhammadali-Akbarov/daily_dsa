"""
graph data structure.
"""
import unittest

from collections import deque
from collections import defaultdict


class Graph:
    """
    the graph data structure.
    """
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """
        add a new edge to the graph.
        """
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        """
        breadth-first search.
        """
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                result.append(vertex)
                visited.add(vertex)
                queue.extend(self.graph[vertex])

        return result

    def dfs(self, start):
        """
        depth-first search.
        """
        visited = set()
        stack = [start]
        result = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                result.append(vertex)
                visited.add(vertex)
                stack.extend(
                    neighbor for neighbor in self.graph[vertex]
                    if neighbor not in visited
                )

        return result


class TestGraph(unittest.TestCase):
    """
    the test graph class.
    """
    def setUp(self):
        """
        setting-up the test graph class.
        """
        self.graph = Graph()

    def test_add_edge(self):
        """
        the test add edge method.
        """
        self.graph.add_edge("A", "B")
        self.graph.add_edge("B", "C")
        self.assertEqual(
            self.graph.graph,
            {"A": ["B"], "B": ["A", "C"], "C": ["B"]}
        )

    def test_bfs(self):
        """
        the test bfs method.
        """
        self.graph.add_edge("A", "B")
        self.graph.add_edge("B", "C")
        self.graph.add_edge("C", "D")
        self.graph.add_edge("D", "A")

        self.assertEqual(self.graph.bfs("A"), ["A", "B", "D", "C"])

    def test_dfs(self):
        """
        the test drf method.
        """
        self.graph.add_edge("A", "B")
        self.graph.add_edge("B", "C")
        self.graph.add_edge("C", "D")
        self.graph.add_edge("D", "A")

        self.assertEqual(self.graph.dfs("A"), ["A", "D", "C", "B"])


if __name__ == '__main__':
    unittest.main()
