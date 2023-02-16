# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        global res
        if not root:
            return 0
        
        res = 0
        def dfs(node, curStr):
            global res
            if not node.left and not node.right:
                newNum = int(curStr + str(node.val))
                res += newNum
            if node.left:
                dfs(node.left, curStr + str(node.val))
            if node.right:
                dfs(node.right, curStr + str(node.val))
        
        dfs(root, "")

        return res