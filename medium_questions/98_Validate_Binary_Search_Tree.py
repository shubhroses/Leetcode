# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node, low = -math.inf, high = math.inf):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return helper(node.right, node.val, high) and helper(node.left, low, node.val)
        return helper(root)

        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Need a helper function that return true if within bounds?
        lowerbound: -inf
        upperbound: inf

        Update lower and upper bounds when calling function again, based on current node value  
        """
        def helper(node = None, lower = -inf, upper = inf):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            
            left = helper(node.left, lower, node.val)
            right = helper(node.right, node.val, upper)
            return left and right
            

        return helper(root)