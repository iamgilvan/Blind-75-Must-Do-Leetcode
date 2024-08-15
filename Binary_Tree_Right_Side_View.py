from collections import deque
import unittest

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom
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
def binary_tree_right_side_view(root):
    temp_result = []
    def bfs(node, h):
        if not node:
            return

        if len(temp_result) <= h:
            temp_result.append([])
        temp_result[h].append(node.key)

        bfs(node.left, h + 1)
        bfs(node.right, h + 1)

    bfs(root.root, 0)
    res = []
    for i in temp_result:
        if len(i) > 1:
            res.append(i[-1])
        else:
            res.append(i[0])
    return res

def binary_tree_right_side_view_ii(root):
    result = []
    def bfs(node, h):
        if not node:
            return

        if len(result) <= h:
            result.append(0)

        bfs(node.left, h + 1)
        bfs(node.right, h + 1)
        result[h] = node.key

    bfs(root.root, 0)
    return result

class TestCase(unittest.TestCase):
    def test_binary_tree_right_side_view(self):
        t = BinaryTree()
        n1 = t.insert(1, None)
        n2= t.insert(2, n1)
        n3 = t.insert(3, n1)
        t.insert(4, n3)
        t.insert(5, n2)

        assert binary_tree_right_side_view(t) == [1,3,4]
        assert binary_tree_right_side_view_ii(t) == [1,3,4]
if __name__ == "__main__":
    unittest.main()