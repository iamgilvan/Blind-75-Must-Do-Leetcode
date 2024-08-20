# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.
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


