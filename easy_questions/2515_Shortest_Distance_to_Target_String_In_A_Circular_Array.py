class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        """
        Find index of target in words
        
        if not in words: return -1
        
        return min(abs(ind - target), len(ind))
        
        start = 1
        targetInd = 4
        
        abs(start-targetInd) = 3
        
        abs(start+n - targetInd) = 2
        """
        n = len(words)
        count = 0
        for _ in range(startIndex, startIndex + n): 
            left = words[(startIndex - count)%n]
            right = words[(startIndex + count)%n]
            print(f"left: {left}")
            print(f"right: {right}")
            if left == target or right == target:
                return count
            count += 1
        return -1