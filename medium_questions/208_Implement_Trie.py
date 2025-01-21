class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.word=False
        self.children={}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node=self.root
        for i in word:
            if i not in node.children:
                node.children[i]=TrieNode()
            node=node.children[i]
        node.word=True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node=self.root
        for i in word:
            if i not in node.children:
                return False
            node=node.children[i]
        return node.word

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node=self.root
        for i in prefix:
            if i not in node.children:
                return False
            node=node.children[i]
        return True
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")


class Node:
    def __init__(self):
        # Store children in a dictionary
        self.dict = {}
        self.isLast = False

class Trie:

    def __init__(self):
        # Initialize the trie with a root node
        self.trie = Node()

    def insert(self, word: str) -> None:
        cur = self.trie
        for c in word:
            # If character not yet a child, create a new node
            if c not in cur.dict:
                cur.dict[c] = Node()
            # Move to the child node
            cur = cur.dict[c]
        # Mark the end of a valid word
        cur.isLast = True

    def search(self, word: str) -> bool:
        cur = self.trie
        for c in word:
            # If character not present in children, word not found
            if c not in cur.dict:
                return False
            cur = cur.dict[c]
        # Return True only if we've ended on a terminal node
        return cur.isLast

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for c in prefix:
            if c not in cur.dict:
                return False
            cur = cur.dict[c]
        # If we can follow the prefix through, it exists
        return True
