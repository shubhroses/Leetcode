# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        do dfs and maintain a curMax 
        """
        global res
        res = 0
        def helper(node, curMax):
            global res
            if not node:
                return
            if node.val >= curMax:
                #print(node.val)
                res += 1
            newMax = max(node.val, curMax)
            helper(node.left, newMax)
            helper(node.right, newMax)
        helper(root, float("-inf"))
        return res