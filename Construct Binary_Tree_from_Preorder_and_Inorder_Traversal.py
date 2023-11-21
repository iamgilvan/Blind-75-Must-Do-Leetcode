import unittest

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None
    root_val = preorder[0]
    root = TreeNode(root_val)  # Certifique-se de ter uma classe TreeNode ou algo semelhante

    root_index = inorder.index(root_val)

    root.left = buildTree(preorder[1:1+root_index], inorder[:root_index])
    root.right = buildTree(preorder[1+root_index:], inorder[root_index+1:])

    return root