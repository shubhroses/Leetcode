class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        if letters[i+1] > target and letters[i] <= target:

        """
        l, r = 0, len(letters)-1

        while l <= r:
            m = (r+l)//2
            if m == len(letters)-1:
                break
            if letters[m+1] <= target:
                l = m+1
            elif letters[m] > target:
                r = m-1
            else:
                return letters[m+1]
        return letters[0]