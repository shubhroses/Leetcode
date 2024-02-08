class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Starting at every gate do a bfs, update the empty room to be min of its current value and layer in bfs
        """
        gates = []
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    gates.append((r, c))
        
        queue = collections.deque(gates)

        visited = set()
        level = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r < 0 or r >= len(rooms) or c < 0 or c >= len(rooms[0]) or rooms[r][c] == -1 or (r, c) in visited:
                    continue
                rooms[r][c] = min(rooms[r][c], level)
                visited.add((r, c))
                queue.append((r-1, c))
                queue.append((r+1, c))
                queue.append((r, c-1))
                queue.append((r, c+1))
            level += 1


        