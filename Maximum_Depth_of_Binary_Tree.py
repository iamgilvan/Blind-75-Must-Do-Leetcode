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

def binary_tree_max_depth(root):
    def get_max_depth(node, h):
        if not node:
            return h

        level_l = get_max_depth(node.left, h + 1)
        level_r = get_max_depth(node.right, h + 1)

        return max(level_l, level_r)
    return get_max_depth(root.root, 0)

class TestCase(unittest.TestCase):
    def test_binary_tree_max_depth(self):
        t = BinaryTree()
        n1 = t.insert(3, None)
        t.insert(9, n1)
        n3 = t.insert(20, n1)
        t.insert(15, n3)
        t.insert(7, n3)

        max = binary_tree_max_depth(t)
        assert max == 3

if __name__ == "__main__":
    unittest.main()