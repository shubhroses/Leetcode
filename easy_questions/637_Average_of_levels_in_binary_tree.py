# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = deque([root])
        if not root:
            return res

        while q:
            cur = 0
            count = 0
            for _ in range(len(q)):
                top = q.popleft()
                cur += top.val
                count += 1
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
            res.append(cur/count)
        return res