# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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