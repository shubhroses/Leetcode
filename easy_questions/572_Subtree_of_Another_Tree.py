# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Write same tree,
        from each node of root, run same tree until true
        """
        def sameTree(left, right):
            if not left and not right:
                return True
            if (left and not right) or (right and not left) or (left.val != right.val):
                return False
            
            return sameTree(left.left, right.left) and sameTree(left.right, right.right)
        

        if sameTree(root, subRoot):
            return True 
        if not root:
            return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        # 572_Subtree_of_Another_Tree.py

            
