class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        Look at substrings of length len(words)*len(words[0])
        If each word can be broken 
        """

        c1 = {}
        for word in words:
            c1[word] = c1.get(word, 0) + 1
            
        lenSubstr = len(words)*len(words[0])
        lenWord = len(words[0])
        res = []

        for l in range(0, len(s) - lenSubstr+ 1):
            c2 = {}
            for i in range(l, l + lenSubstr, lenWord):
                word = s[i:i+lenWord]
                c2[word] = c2.get(word,0) + 1
            if c1 == c2:
                res.append(l)
        return res