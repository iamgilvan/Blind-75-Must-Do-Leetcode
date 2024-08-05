from collections import deque
import unittest

# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# Example 1:

# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Example 2:

# Input: root = [1,2]
# Output: 1

class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, parent=None):
        new_node = Node(key)
        if parent is None:
            if self.root is not None:
                raise Exception("A root already exists")
            self.root = new_node
            return new_node

        if not parent.left:
            parent.left = new_node
            new_node.parent = parent
        elif not parent.right:
            parent.right = new_node
            new_node.parent = parent
        else:
            raise Exception("A node cannot have more than two children")
        return new_node
# O(n) time
# O(h) space
# DFS
def diameter_of_a_binary_tree(root):
    res = [0]
    def dfs(node):
        if not node:
            return -1

        l = dfs(node.left)
        r = dfs(node.right)
        res[0] = max(res[0], 2 + l + r)
        return 1 + max(l, r)
    dfs(root.root)
    return res[0]

class TestCase(unittest.TestCase):
    def test_diameter_of_a_binary_tree(self):
        t = BinaryTree()
        n1 = t.insert(3, None)
        t.insert(9, n1)
        n3 = t.insert(20, n1)
        t.insert(15, n3)
        t.insert(7, n3)

        assert 3 == diameter_of_a_binary_tree(t)

if __name__ == "__main__":
    unittest.main()