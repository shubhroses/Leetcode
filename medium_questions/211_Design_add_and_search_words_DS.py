class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = 0
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()      

    def addWord(self, word):
        root = self.root
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
        root.end_node = 1
        
    def search(self, word):
        def dfs(node, i):
            if i == len(word): return node.end_node
               
            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i+1): return True
                    
            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)
            
            return False
    
        return dfs(self.root, 0)



"""
To add a word need a node with dictionary, letter, and isLast

add:
    for c in Word
        if c in dictionary, go to next letter and next node
        if c not in dictionary, add to dictinary and create a new node 
    set is word to true

search:
    for c in word:
        if c is ., let next be any element in dict
    if is word return

    bad
    i

    start = ({'b': }, False) 
    ({a: }, False)
    ({d}, False)
    ({}, True) cur


"""
class Node:
    def __init__(self):
        self.dict = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.start = Node()

    def addWord(self, word: str) -> None:
        cur = self.start
        for c in word:
            if c not in cur.dict:
                cur.dict[c] = Node()
            cur = cur.dict[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        def isInDict(cur, i):
            if i == len(word):
                return cur.isWord
            if word[i] != '.':
                if word[i] not in cur.dict:
                    return False
                else:
                    return isInDict(cur.dict[word[i]], i + 1)
            else:
                for k, v in cur.dict.items():
                    if isInDict(cur.dict[k], i + 1):
                        return True
                return False
        
        return isInDict(self.start, 0)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
