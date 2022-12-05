class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()

        firstLetter = sentence[0][0]
        lastLetter = sentence[0][-1]
        i = 1
        while i < len(sentence):
            curword = sentence[i]
            curFirstLetter = curword[0]
            if curFirstLetter != lastLetter:
                return False
            lastLetter = curword[-1]
            i+=1
        
        if firstLetter != lastLetter:
            return False
        return True
    
    """
    sentence = [leetcode exercises sound delightful]
                                              i
    firstLetter = l
    
    
    lastLetter = l
    curFirstLetter = d
    
    len(sentence = 1)
    
    """