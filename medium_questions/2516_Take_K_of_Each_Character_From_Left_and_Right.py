class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        ra = s.count('a') - k
        rb = s.count('b') - k
        rc = s.count('c') - k
        
        if any(i < 0 for i in [ra, rb, rc]):
            return -1
        
        hm = defaultdict(int)
        l = j = res = 0
        
        for i in s:
            hm[i] += 1
            l += 1
            
            while hm['a'] > ra or hm['b'] > rb or hm['c'] > rc:
                hm[s[j]] -= 1
                l -= 1
                j += 1
            
            res = max(res, l)
        
        return len(s) - res