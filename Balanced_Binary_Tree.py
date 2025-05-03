from typing import Optional

# Given a binary tree, determine if it is
# height-balanced.

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:

# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:

# Input: root = []
# Output: true


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# O(n) time
# O(h) space
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)

            if abs(l - r) > 1:
                return -1
            return max(l, r) + 1
        cur = root
        h = dfs(cur)
        return True if h > -1 else False