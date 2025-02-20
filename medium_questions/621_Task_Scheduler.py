class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1
        
        frequencies.sort()

        # max frequency
        f_max = frequencies.pop()
        idle_time = (f_max - 1) * n
        
        while frequencies and idle_time > 0:
            idle_time -= min(f_max - 1, frequencies.pop())
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)

class Solution: 
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        For duplicates add n to subsequent ones
        Add all to heap (0, 'A')
        """
        h = []
        charToCount = collections.defaultdict(int)
        for t in tasks:
            heapq.heappush(h, (charToCount[t], t))
            charToCount[t] += (n+1)
        i = 0
        while h:
            if i >= h[0][0]:
                heapq.heappop(h)
            i += 1
        return i
