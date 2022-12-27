# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        """
        Run is sameTre on the all the nodes of root and 
        """

        def is_identical(node1, node2):

            if node1 is None or node2 is None:
                return node1 is None and node2 is None

            if node1.val != node2.val:
                return False
            return is_identical(node1.left, node2.left) and is_identical(node1.right, node2.right)

        def dfs(node):
            if node is None:
                return False
            elif is_identical(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)
        return dfs(root)