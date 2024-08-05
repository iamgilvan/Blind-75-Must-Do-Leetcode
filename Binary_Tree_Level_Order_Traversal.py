from collections import deque
import unittest

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
def binary_tree_order_level(root):
    result = []
    def traverse(node, h):
        if not node:
            return

        if len(result) <= h:
            result.append([])
        result[h].append(node.key)

        traverse(node.left, h + 1)
        traverse(node.right, h + 1)

    traverse(root.root, 0)
    return result
# O(n) time
# O(h) space
def binary_tree_order_level_iterative(root):
    result = []
    q = deque([root.root])
    l = 0
    while q:
        result.append([])
        for i in range(len(q)):
            node = q.popleft()
            if node:
                result[l].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            elif len(result[-1]) == 0:
                del result[-1]
        l += 1
    return result

class TestCase(unittest.TestCase):
    def test_binary_tree_order_level(self):
        t = BinaryTree()
        n1 = t.insert(3, None)
        t.insert(9, n1)
        n3 = t.insert(20, n1)
        t.insert(15, n3)
        t.insert(7, n3)

        assert binary_tree_order_level(t) == [[3],[9,20],[15,7]]
        assert binary_tree_order_level_iterative(t) == [[3],[9,20],[15,7]]

if __name__ == "__main__":
    unittest.main()