class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        anagramToString = {abc:[bac, cab], ...}
        return [[bac, cab], ...]
        """
        anagramToStr = collections.defaultdict(list)
        for string in strs:
            elements = "".join(sorted(string))
            anagramToStr[elements].append(string)
        return anagramToStr.values()
