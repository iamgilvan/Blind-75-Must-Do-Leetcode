# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#TC O(n^2)
#TS O(h)
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root and subRoot: return False

        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    
    def sameTree(self, t, s):
        if not t and not s:
            return True

        if t and s and s.val == t.val:
            return (self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right))

        return False