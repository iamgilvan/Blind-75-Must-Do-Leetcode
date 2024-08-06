# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = None  # Variável para armazenar o resultado

        def dfs(node, idx):
            nonlocal k

            if not node or idx > k:
                return idx

            # Visite o nó da esquerda
            idx = dfs(node.left, idx)

            # Processar o nó atual
            idx += 1
            if idx == k:
                self.result = node.val
                return idx  # Parar a recursão

            # Visite o nó da direita
            idx = dfs(node.right, idx)

            return idx

        dfs(root, 0)
        return self.result
    # TC: O(n)
    # TS: O(n)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            self.result.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return self.result[k-1]