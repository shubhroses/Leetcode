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

# test
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Do level order traversal, keep count, if find node withough left or right return count
        """
        q = deque([root])

        if not root:
            return 0

        count = 1

        while q:
            for _ in range(len(q)):
                top = q.popleft()
                if not top.left and not top.right:
                    return count
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
            count += 1
        return 0