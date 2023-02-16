# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curPath):
            if node is None:
                return 0
            curPath.append(node.val)
            pathCount, pathSum = 0, 0

            for i in range(len(curPath)-1, -1, -1):
                pathSum += curPath[i]
                if pathSum == targetSum:
                    pathCount += 1
            
            pathCount += dfs(node.left, curPath)
            pathCount += dfs(node.right, curPath)

            del curPath[-1]
            return pathCount

        return dfs(root, [])