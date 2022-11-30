class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        
        n = len(s)
        c = Counter(s)
        cur = ""
        heap = []
        
        reAdd = deque()
        
        for char, count in c.items():
            heapq.heappush(heap, (-count, char))
        
        for i in range(n):
            if reAdd and reAdd[0][1] == i:
                character, index = reAdd.popleft()
                heapq.heappush(heap, (-1*c[character], character))
            if not heap:
                return ""
                
            count, char = heapq.heappop(heap)
            count *= -1
            if count > 1:
                reAdd.append((char, i+k))
            c[char] -= 1
            if c[char] == 0:
                del c[char]
            cur += char
        return cur
        
        """
        s = aabbcc
        k = 3
        
        i = 0
        c = {a:2, b:2, c:2}
        heap = {(-2, a), (-2, b), (-2, c)}
        readd = []
        cur = ""
        
        i = 1
        c = {a:1, b:2, c:2}
        heap = {(-2, b), (-2, c)}
        readd = [(a, 3)]
        cur = "a"
        
        i = 2
        c = {a:1, b:1, c:1}
        heap = {(-2, c)}
        readd = [(a, 3),(b, 4)]
        cur = "ab"
        
        i = 3
        c = {a:1, b:1, c:1}
        heap = {(-1, a)}
        readd = [(b, 4) ,(c, 5)]
        cur = "abc"
        
        i = 4
        c = {b:1, c:1}
        heap = {(-1, b)}
        readd = [(c, 5)]
        cur = "abca"
        
        i = 5
        c = {c:1}
        heap = {(-1, c)}
        readd = []
        cur = "abcab"
        
        i = 5
        c = {c:1}
        heap = {}
        readd = []
        cur = "abcabc"

        maintain heap ordered by count:
            when pop from heap, dont add to heap until k indexes pass
            after k indexes add back to heap and reheapify
        """
        

"""
n = 6
s = aabbcc
k = 3
cur = ""
c = {a:2, b:2, c:2}


i = 0
c = {a:1, b:2, c:2}
heap = {(-2, b), (-2, c)}
count = 2
char = a
reAdd = [(a, 2)]
cur = "a"

i = 1
c = {a:1, b:1, c:2}
heap = {(-2, c)}
count = 2
char = b
reAdd = [(a, 3), (b, 4)]
cur = "ab"

i = 2
c = {a:1, b:1, c:1}
heap = {}
count = 2
char = c
reAdd = [(a, 3), (b, 4), (c, 5)]
cur = "abc"

i = 3
c = {b:1, c:1}
heap = {}
count = 1
char = a
reAdd = [(b, 4), (c, 5)]
    character = a
    index = 3
cur = "abca"

i = 4
c = {c:1}
heap = {}
count = 1
char = b
reAdd = [(c, 5)]
    character = b
    index = 4
cur = "abcab"

i = 5
c = {c:1}
heap = {}
count = 1
char = c
reAdd = []
    character = c
    index = 5
cur = "abcabc"














i = 2
c = {a:1, b:1, c:1}
heap = {(-2, c)}
reAdd = [(a, 3),(b, 4)]
cur = "ab"

i = 3
c = {a:1, b:1, c:1}
heap = {(-1, a)}
reAdd = [(b, 4) ,(c, 5)]
cur = "abc"

i = 4
c = {b:1, c:1}
heap = {(-1, b)}
reAdd = [(c, 5)]
cur = "abca"

i = 5
c = {c:1}
heap = {(-1, c)}
reAdd = []
cur = "abcab"

i = 5
c = {c:1}
heap = {}
reAdd = []
cur = "abcabc"

maintain heap ordered by count:
    when pop from heap, dont add to heap until k indexes pass
    after k indexes add back to heap and reheapify
"""