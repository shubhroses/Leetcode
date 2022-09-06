# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
In order traversal
stack = [2, 1, 3]
visited = {1, 2}

top = 1

res = [2, ]

"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        If we are starting at a node we can only split once
        
        Brute force: for every single node consider it as root
            Find max path from left subtree where no splitting is allowed
            Find max path from right subtree where non splitting is allowed
            
            
        compute if allowed to split, and if not allowed to split
        """
        global res
        res = float("-inf")
        
        def dfs(node):
            global res
            if not node:
                return 0
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)
            
            res = max(res, node.val + leftMax + rightMax)
            
            return node.val + max(leftMax, rightMax)
        
        dfs(root)
        return res