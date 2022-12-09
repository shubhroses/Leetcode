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