class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1 or k == len(weights):
            return 0
        
        m = sorted(weights[i] + weights[i+1] for i in range(len(weights)-1))
        
        return sum(m[-k+1:]) - sum(m[:k-1])