# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False
        if p.val == q.val:
            return (self.isSameTree(p.left, q.left)) and \
               (self.isSameTree(p.right, q.right))
        return False

        if (p and not q) or (not p and q):
            return False
        if not p and not q:
            return True
        if p.val == q.val:
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            return left and right
        return False


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if (p and not q) or (q and not p) or (p.val != q.val):
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
