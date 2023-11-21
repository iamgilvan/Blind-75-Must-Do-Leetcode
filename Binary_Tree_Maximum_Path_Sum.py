# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(n) time
# O(h) space
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_v = root.val
        def dfs(node):
            nonlocal max_v
            if not node:
                return 0

            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            max_v = max(max_v, leftMax + rightMax + node.val)
            return node.val + max(leftMax, rightMax)
        dfs(root)
        return max_v


