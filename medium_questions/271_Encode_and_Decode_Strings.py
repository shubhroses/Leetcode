class Codec:
    """
    strs = ["big", "horse"]
    res = "3:big5:horse"

    string = "horse"
    num = 5

         012345678901
    s = "3:big5:horse"
                    j
            i
    res = ["big", "horse"]
    num = 5

    """
    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            num = len(string)
            res += str(num)
            res += ":"
            res += string
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        j = 0
        while j < len(s):
            i = j
            while s[i] != ":":
                i += 1
            num = int(s[j:i])
            res.append(s[i+1:i+num+1])
            j = i+num+1
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))