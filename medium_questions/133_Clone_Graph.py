class Solution: 
    def cloneGraph(self, node: 'Node') -> 'Node':
        # bfs iteratively
        if not node:
            return
        nodeCopy = Node(node.val, [])
        dic = {node: nodeCopy} # old to new
        queue = collections.deque([node])

        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = Node(neighbor.val, [])
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy

        # dfs iteratively
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        nodeCopy = Node(node.val, [])
        dic = {node: nodeCopy} # old to new

        def dfs(node):
            if not node:
                return
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = Node(neighbor.val, [])
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    dfs(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        dfs(node)
        return nodeCopy