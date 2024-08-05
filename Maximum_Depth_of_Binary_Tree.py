from collections import deque
import unittest

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

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
def binary_tree_max_depth_dfs(root):
    def get_max_depth(node, h):
        if not node:
            return h

        level_l = get_max_depth(node.left, h + 1)
        level_r = get_max_depth(node.right, h + 1)

        return max(level_l, level_r)
    curr = root.root
    return get_max_depth(curr, 0)

# O(n) time
# O(h) space
# BFS
def binary_tree_max_depth_bfs(root):
    if not root:
        return 0
    q = deque([root.root])
    level = 0
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        level += 1
    return level

# O(n) time
# O(h) space
# DFS
def binary_tree_max_depth_iterative_dfs(root):
    if not root:
        return 0
    stack = [[root.root, 1]]
    res = 0
    while stack:
        node, depth = stack.pop()
        if node:
            res = max(res, depth)
            stack.append([node.right, depth + 1])
            stack.append([node.left, depth + 1])
    return res

class TestCase(unittest.TestCase):
    def test_binary_tree_max_depth(self):
        t = BinaryTree()
        n1 = t.insert(3, None)
        t.insert(9, n1)
        n3 = t.insert(20, n1)
        t.insert(15, n3)
        t.insert(7, n3)

        assert 3 == binary_tree_max_depth_dfs(t)
        assert 3 == binary_tree_max_depth_bfs(t)
        assert 3 == binary_tree_max_depth_iterative_dfs(t)

if __name__ == "__main__":
    unittest.main()