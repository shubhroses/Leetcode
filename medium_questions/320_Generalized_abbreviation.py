class AbbreviatedWord:
    def __init__(self, str, start, count):
        self.str = str
        self.start = start
        self.count = count

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        wordLen = len(word)
        result = []
        queue = deque()
        queue.append(AbbreviatedWord(list(), 0, 0))
        while queue:
            abWord = queue.popleft()
            if abWord.start == wordLen:
                if abWord.count != 0:
                    abWord.str.append(str(abWord.count))
                result.append(''.join(abWord.str))
            else:
                queue.append(AbbreviatedWord(list(abWord.str), abWord.start + 1, abWord.count + 1))
                if abWord.count != 0:
                    abWord.str.append(str(abWord.count))
                newWord = list(abWord.str)
                newWord.append(word[abWord.start])
                queue.append(AbbreviatedWord(newWord, abWord.start + 1, 0))
        return result 
