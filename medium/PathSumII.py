class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        result = []

        def dfs(node, remaining, path):

            if not node:
                return

            path = path + [node.val]
            remaining -= node.val

            #Cuando termina el arbol

            if not node.right and not node.left and remaining == 0:
                result.append(path)
                return


            dfs(node.left, remaining, path)
            dfs(node.right, remaining, path)

        dfs(root, targetSum, [])
        return result    