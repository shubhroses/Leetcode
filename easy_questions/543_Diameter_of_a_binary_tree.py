# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node):
            if not node:
                return 0
            nonlocal diameter
            leftTree = dfs(node.left)
            rightTree = dfs(node.right)
            diameter = max(diameter, leftTree + rightTree )
            return max(leftTree, rightTree) + 1
        dfs(root)
        return diameter

"""
Difficulty: Forgot to call dfs function
 learned to uses nonlocal to use a variable in a function that is first created in parent function
"""