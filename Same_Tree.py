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