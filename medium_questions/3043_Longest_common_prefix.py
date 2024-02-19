class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def insert_into_trie(root, number):
            node = root
            for digit in str(number):
                if digit not in node.children:
                    node.children[digit] = TrieNode()
                node = node.children[digit]
            node.is_end_of_word = True

        def longest_common_prefix_in_trie(root, number):
            node = root
            length = 0
            for digit in str(number):
                if digit in node.children:
                    length += 1
                    node = node.children[digit]
                else:
                    break
            return length
        
        trie_root = TrieNode()
        for number in arr1:
            insert_into_trie(trie_root, number)

        max_length = 0
        for number in arr2:
            max_length = max(max_length, longest_common_prefix_in_trie(trie_root, number))

        return max_length
                           
