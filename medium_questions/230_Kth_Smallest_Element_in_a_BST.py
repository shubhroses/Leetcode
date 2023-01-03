# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k-=1 
            if not k:
                return root.val
            root = root.right

        # Recursive
        """
        Do in order traversal 
        """
        self.K = k
        def helper(node):
            if not node:
                return
            helper(node.left)
            self.K -= 1
            if self.K == 0:
                self.res = node.val
                return
            helper(node.right)

        self.res = None
        helper(root)
        return self.res   