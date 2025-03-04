class Solution(object): 
    def isBalanced(self, root):
        return (self.Height(root) >= 0)
    def Height(self, root):
        if root is None:  return 0
        leftheight, rightheight = self.Height(root.left), self.Height(root.right)
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:  return -1
        return max(leftheight, rightheight) + 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Helper function that returns depth
        if they differ 
        """
        self.res = True

        def helper(node):
            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)

            if abs(left - right) > 1:
                self.res = False
                return float("inf")
            
            return max(left, right) + 1

        helper(root)
        return self.res
