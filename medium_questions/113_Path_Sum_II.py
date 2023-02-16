# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printPath(self, arr):
        print([node.val for node in arr])


            
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res = []
        if not root:
            return []

        def dfs(node, curSum, curPath):
            tot = curSum + node.val
            # self.printPath(curPath)
            
            if not node.left and not node.right:
                if tot == targetSum:
                    res.append(curPath + [node.val])
                
            if node.left:
                dfs(node.left, tot, curPath + [node.val])
            if node.right:
                dfs(node.right, tot, curPath + [node.val])
            

        dfs(root, 0, [])
        # self.printRes(res)
        return res