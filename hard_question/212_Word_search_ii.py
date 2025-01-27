class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'

        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[WORD_KEY] = word
        
        rowNum = len(board)
        colNum = len(board[0])

        matchedWords = []

        def backtracking(row, col, parent):
            letter = board[row][col]
            currNode = parent[letter]

            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                matchedWords.append(word_match)
            
            board[row][col] = '#'

            for(rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)
            
            board[row][col] = letter

            if not currNode:
                parent.pop(letter)
        for row in range(rowNum):
            for col in range(colNum):
                if board[row][col] in trie:
                    backtracking(row, col, trie)
        return matchedWords
    



    class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0
    
    def addWord(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True
    
    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Done: Put all words in a trie
        Do dfs on board and find words
        """
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
                or (r, c) in visit
            ):
                return
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                node.isWord = False
                res.add(word)
                root.removeWord(word)

            dfs(r-1, c, node, word) #up
            dfs(r+1, c, node, word) #down
            dfs(r, c-1, node, word) #left
            dfs(r, c+1, node, word) #right
            visit.remove((r, c))

        
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, root, "")
        return list(res)


class trieNode():
    def __init__(self):
        self.dict = {}
        self.isWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Add all words to a trie
        Do a dfs starting at each cell, avoiding visited
        if is word add to output
        """
        node = trieNode()
  
        for word in words:
            cur = node
            for c in word:
                if c not in cur.dict:
                    cur.dict[c] = trieNode()
                cur = cur.dict[c]
            cur.isWord = True
        
        self.visited = set()
        self.res = set()

        def helper(r, c, cur, node):
            if cur and node and node.isWord:
                self.res.add(cur)

            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or (r, c) in self.visited:
                return
            
            # print(r, c, board[r][c], "cur: ", cur, node.dict, node.isWord)



            if board[r][c] not in node.dict:
                return
            
            self.visited.add((r,c))

            newCur = cur + board[r][c]
            helper(r+1, c, newCur, node.dict[board[r][c]])
            helper(r-1, c, newCur, node.dict[board[r][c]])
            helper(r, c+1, newCur, node.dict[board[r][c]])
            helper(r, c-1, newCur, node.dict[board[r][c]])

            self.visited.remove((r,c))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                helper(r, c, "", node)
        
        return list(self.res)
