"""
binary trees are a fundamental data structure in computer science
and are widely used in various applications, a binary tree is a
tree data structure in which each node has at most two children,
referred to as the left child and the right child.

basic concepts of a binary tree:
    1) node - the fundamental part of a binary tree,
       a node contains data and references to its left and right children.
    2) root - the top node of the tree, from which all other nodes descend.
    3) leaf -  a node with no children.
    4) depth - the length of the path from the root to the node.
    5) height - the length of the longest path from the node to a leaf.

basic operations on a binary tree.
    1) insertion - add a new node to the tree,
        the specifics depend on the type of binary tree.
    2) deletion - remove a node from the tree,
        this might involve rearranging the tree to maintain its properties.
    3) traversal - visit all the nodes of the tree, common methods include
        in order, pre order, and post order.
    4) search - find a node in the tree, in a binary search tree, this can be done efficiently.
    5) finding the minimum and maximum: in a binary search tree, this involves going to the
    leftmost or rightmost left, respectively.

complexity analysis:
    search, insertion, deletion in a binary search tree: average case: O(log(n)), worst case:
    O(n) (the worst case occurs when the tree becomes skewed).
    traversal operations: O(n) as they visit every node.
"""


class TreeNode:
    """
    tree nodes.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """
    binary trees.
    """
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def inorder_traversal(self, node, result=None):
        """
        inorder traversal.
        """
        if result is None:
            result = []

        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.data)
            self.inorder_traversal(node.right, result)

        return result
