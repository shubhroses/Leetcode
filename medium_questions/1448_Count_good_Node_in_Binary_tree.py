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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
    2
      4
    10  8
    
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.res = 0

        def helper(node, maxPath):
            if not node:
                return
            
            if node.val >= maxPath:
                self.res += 1
            
            helper(node.left, max(node.val, maxPath))
            helper(node.right, max(node.val, maxPath))

        helper(root, root.val)

        return self.res

