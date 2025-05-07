# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        res = []
        
        if not root: 
            return None
        flag = -1
        while q:
            cur = []
            for _ in range(len(q)):
                top = q.popleft()
                cur.append(top.val)
                if top.right:
                    q.append(top.right)
                if top.left:
                    q.append(top.left)
            res.append(cur[::flag])
            flag *= (-1)
        return res

# test
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        flag = True
        
        q = deque([root])
        while q:
            cur = []
            for _ in range(len(q)):
                next = q.popleft()
                cur.append(next.val)
                if next.left:
                    q.append(next.left)
                if next.right:
                    q.append(next.right)
            if flag:
                res.append(cur)
                flag = False
            else:
                res.append(cur[::-1])
                flag = True
        return res