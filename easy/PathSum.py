# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        
        #Caso 1, no hay arbol
        if not root:
            return False

        #Caso 2, solo hay un nodo

        if not root.left and not root.right:
            return root.val == targetSum

        #Caso 3, arbol construido

        r = targetSum - root.val

        return (self.hasPathSum(root.left, r) or self.hasPathSum(root.right, r))
