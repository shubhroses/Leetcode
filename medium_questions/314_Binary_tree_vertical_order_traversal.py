# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Have the confidence to move forward from creating plan to writing code.
        a:0
        b:-1
        c:1
        d:0
            a
        b       c
               d
       adj = {-1:[b],
              0: [a, d],
              1: [c]}
        
            a
          b   c
        d
        
        a
        dist = 0
        
        
        adj = {0:[a],
                -1:[b],
                -2:[d],
                1:[c]}

          [[d], [b], [a], [c]]
        """
        columnTable = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        while queue:
            node, column = queue.popleft()
            if node is not None:
                columnTable[column].append(node.val)
                queue.append((node.left, column-1))
                queue.append((node.right, column +1))
        return [columnTable[x] for x in sorted(columnTable.keys())]

        queue = deque([(root, 0)])
        adj_list = collections.defaultdict(list)
        mn, mx = float("inf"), float("-inf")
        while queue:
            top, dist = queue.popleft()
            if top:
                queue.append((top.left, dist-1))
                queue.append((top.right, dist+1))
                adj_list[dist].append(top.val)
                mn, mx = min(mn, dist), max(mx, dist)
        res = []
        if mn == float("inf") or mx == float("-inf"):
            return []
        for i in range(int(mn), int(mx+1)):
            res.append(adj_list[i])
        return res