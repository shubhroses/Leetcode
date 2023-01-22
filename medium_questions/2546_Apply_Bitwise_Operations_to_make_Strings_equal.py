class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        """
        or: of either of them are 1 then set to 1
        xor: one must be 1 and other must be 0
        
        i j    i j
        0 0 -> 0 0
        1 0 -> 1 1
        0 1 -> 1 1
        1 1 -> 1 0
        
        case 1:
            if there is only 1s in s and only 0s in t False
            if there is only 0s in s and only 1s in t False
            if there are both 1s and 0s in s and both 1s and zeros in 
            
            
        """
        if s == target:
            return True
        
        sSet = set([c for c in s])
        tSet = set([c for c in target])
        
        print(len(tSet) == 1, len(sSet) >1, list(tSet)[0] == "0")
        if len(tSet) == 1 and list(tSet)[0] == "0" and len(sSet) > 1:
            return False
        elif len(sSet) == 1 and list(sSet)[0] == "0" and len(tSet) > 1:
            return False
        elif len(sSet) > 1 or len(tSet) > 1:
            return True
        return False