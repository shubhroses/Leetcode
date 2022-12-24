# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BFS
        with queue
        """
        if not root:
            return None
        q = collections.deque()
        q.append(root)
        
        res = []
        while q:
            cur = []
            for _ in range(len(q)):
                top = q.popleft()
                cur.append(top.val)
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
            res.append(cur)
        return res

        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        res = []

        if not root:
            return []

        """
        Level order traversal uses bfs, so have to use a queue

        """
        q = collections.deque()
        q.append(root)

        while q:
            cur = []
            for _ in range(len(q)):
                top = q.popleft()
                cur.append(top.val)

                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
            res.append(cur)
        return res
