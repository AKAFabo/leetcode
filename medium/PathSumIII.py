# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        if not root:
            return 0

        # caminos que empiezan aquí + los que empiezan en algún nodo de la izquierda + los de la derecha
        return (self.count_from(root, targetSum)
                + self.pathSum(root.left, targetSum)
                + self.pathSum(root.right, targetSum))

    def count_from(self, node, remaining):
        # Cuenta caminos que EMPIEZAN en node y bajan
        if not node:
            return 0

        count = 0
        if node.val == remaining:      # el camino puede terminar aquí
            count = 1

        # o puede seguir bajando, con lo que queda
        count += self.count_from(node.left, remaining - node.val)
        count += self.count_from(node.right, remaining - node.val)
        return count