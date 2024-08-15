from collections import deque
import heapq
import unittest

# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.
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
def count_good_nodes(root):
    def bfs(node, max_v=float('-inf')):
        if not node:
            return 0

        max_v = max(max_v, node.key)
        res = 1 if node.key >= max_v else 0
        res += bfs(node.left, max_v)
        res += bfs(node.right, max_v)
        return res

    return bfs(root.root)

class TestCase(unittest.TestCase):
    def test_count_good_nodes_in_binary_tree(self):
        t = BinaryTree()
        n1 = t.insert(3, None)
        n2= t.insert(1, n1)
        t.insert(3, n2)
        n3 = t.insert(4, n1)
        t.insert(1, n3)
        t.insert(5, n3)

        assert count_good_nodes(t) == 4
if __name__ == "__main__":
    unittest.main()