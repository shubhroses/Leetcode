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
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Do In order traversal 
        Maintain count

        """
        self.res = -1
        self.count = 1
        def helper(node):
            if not node:
                return
            helper(node.left)
            if self.count == k:
                self.res = node.val
            self.count += 1
            helper(node.right)
            
        helper(root)
        return self.res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        In order traversal, k times

        inorder traversal is dfs
        """
        self.res = None

        def inOrderTraversal(node, iter):
            if not node:
                return 0
            
            left = inOrderTraversal(node.left, iter)

            if left + 1 + iter == k:
                if not self.res:
                    self.res = node.val
                return float("inf")

            right = inOrderTraversal(node.right, left + 1 + iter)

            return left + right + 1
        
        inOrderTraversal(root, 0)
        
        return self.res

