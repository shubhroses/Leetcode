# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return inf
            if not node.left and not node.right:
                return 1
            return min(1+helper(node.right), 1+helper(node.left))
        res = helper(root)
        if res == inf:
            return 0
        return res