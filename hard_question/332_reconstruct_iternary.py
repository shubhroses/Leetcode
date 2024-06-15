from collections import defaultdict
import heapq
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create an adjacency list where each node has a min-heap of destinations
        adj = defaultdict(list)
        for src, tar in tickets:
            heapq.heappush(adj[src], tar)
        
        res = []
        stack = ["JFK"]
        
        while stack:
            while adj[stack[-1]]:
                # Push the smallest lexical destination onto the stack
                stack.append(heapq.heappop(adj[stack[-1]]))
            # Append the last element of the stack to the result when there are no more destinations
            res.append(stack.pop())
        
        # Return the result in reverse order
        return res[::-1]

# Example usage:
# sol = Solution()
# print(sol.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))