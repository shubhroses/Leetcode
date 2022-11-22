class Solution:
    def minimumKeypresses(self, s: str) -> int:
        c = {}
        for char in s:
            c[char] = c.get(char, 0) + 1

        ans = cnt = 0
        for i, freq in enumerate(sorted(c.values(), reverse=True)):
            if i % 9 == 0:
                cnt += 1
            ans += cnt * freq
        return ans

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        """
        Take the first 9 most common letters and assign them 1
        Take the next 9 most common letters and assign them 2
        Take the next 9 most common letters and assign them 3
        
        Iterate through s and add up counts
        
        apple
        
        counter = {a:1, p:2, l:1, e:1}
        
        [p, a, l, e]
        get the keys sorted by the values 
        
        letterToCount: {p:1, a:1, l:1, e:2}
        
        1. Create counter
        2. 
        
        """
        counter = {}
        for l in s:
            counter[l] = counter.get(l, 0) + 1
        letterToCount = {}
        num = 1
        curCount = 1
        for l, c in sorted(counter.items(), key=lambda x:x[1], reverse=True):
            letterToCount[l] = curCount
            if num%9 == 0:
                curCount += 1
            num+=1
        res = 0
        for l in s:
            res += letterToCount[l]
        return res