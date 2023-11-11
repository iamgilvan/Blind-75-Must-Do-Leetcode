import unittest

class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)
        # check if a new node
        if self.root is None:
            self.root = new_node
            return

        current_node = self.root
        while current_node:
            # check existing key
            if current_node.key == key:
                return
            # iterate over left side
            if key < current_node.key:
                if current_node.left is None:
                    current_node.left = new_node
                    new_node.parent = current_node
                    return
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    new_node.parent = current_node
                    return
                current_node = current_node.right

# O(n) time
# O(h) space
def is_binary_search_tree(root):
    def is_bst(node, min_value=float('-inf'), max_value=float('inf')):
        if not node:
            return True

        if not (min_value < node.key < max_value):
            return False

        result_l = is_bst(node.left, min_value, node.key)
        result_r = is_bst(node.right, node.key, max_value)

        return result_l and result_r

    return is_bst(root.root)
class TestCase(unittest.TestCase):
    def test_is_binary_search_tree(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(4)
        bst.insert(6)
        bst.insert(3)
        bst.insert(7)

        isBst = is_binary_search_tree(bst)
        assert isBst

if __name__ == "__main__":
    unittest.main()