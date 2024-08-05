# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:

# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:

# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:

# Input: p = [1,2,1], q = [1,1,2]
# Output: false


# Definition for a binary tree node.
# TC: O(n)
# EC: O(h)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def get_tree_values(p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return get_tree_values(p.left, q.left) and get_tree_values(p.right, q.right)
    return get_tree_values(p, q)