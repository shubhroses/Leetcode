class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutations = deque()
        permutations.append([])
        numsLength= len(nums)

        for currentNumber in nums:
            n = len(permutations)
            for _ in range(n):
                oldPermutation = permutations.popleft()
                for j in range(len(oldPermutation) + 1):
                    newPermutation = list(oldPermutation)
                    newPermutation.insert(j, currentNumber)
                    if len(newPermutation) == numsLength:
                        res.append(newPermutation)
                    else:
                        permutations.append(newPermutation)
        return res

        """
        res = [[], [1]]

        [1, 2, 3]
            c

        """