# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        q = [(root, 0)]
        
        while q:
            new = []
            d = defaultdict(list)
            print(q)
            for node, index in q:
                d[index].append(node.val)
                if node.left:
                    new.append((node.left, index-1))
                if node.right:
                    new.append((node.right, index+1))
            for i in d:
                res[i].extend(sorted(d[i]))
            q = new
        return [res[i] for i in sorted(res)]
        
        
        g = collections.defaultdict(list) 
        queue = [(root,0)]
        while queue:
            new = []
            d = collections.defaultdict(list)
            for node, s in queue:
                d[s].append(node.val) 
                if node.left:  new += (node.left, s-1), 
                if node.right: new += (node.right,s+1),  
            for i in d: g[i].extend(sorted(d[i]))
            queue = new
        return [g[i] for i in sorted(g)]
        
        """
        Do bfs 
        {ind: row} mapping, maitain min and max
        can return min-max array 
        
          3
        2.  1
      4.5   7.8
      
      [(2, -1), (1, 1)]
          t
      cur = 2
      index = -1
          
      res = {0:[3], -1:[2]}
      
      How to determine if two nodes are at the same position
        """
        
        q = collections.deque()
        q.append((root, 0))
        res = collections.defaultdict(list) 
        mn, mx = inf, -inf
        
        """
        index : []
        
        (x, y) : []
        
        maintain 
        
        """
        
        while q:
            for _ in range(len(q)):
                cur, index = q.popleft()
                mn = min(index, mn)
                mx = max(index, mx)
                
                res[index].append((cur.val))
                if cur.left:
                    q.append((cur.left, index-1))
                if cur.right:
                    q.append((cur.right, index+1))
        result = []
        for i in range(mn, mx+1):
            result.append(res[i])
        return result
