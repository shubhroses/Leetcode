# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        if not root:
            return arr == []

        def dfs(node, curPath):
            if not node.left and not node.right:
                # print(curPath + [node.val])
                if arr == curPath + [node.val]:
                    return True
            left, right = False, False
            if node.left:
                left = dfs(node.left, curPath + [node.val])
            if node.right:
                right = dfs(node.right, curPath + [node.val])
            return left or right

        return dfs(root, [])