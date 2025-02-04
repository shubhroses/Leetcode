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


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Each element can be the first element
        Of remaining elements. each element can be second element

        nums = [0, 1]
        res = []

        cands = [0,1]
        cur = []

            cands = [1]
            cur = [0]

                cands = []
                cur = [0, 1]


            cands = [0]
            cur = [1]

                cands = []
                cur = [1, 0]
        """

        self.res = []

        def helper(cands, cur):
            if not cands:
                self.res.append(cur)
                return
            for i, e in enumerate(cands):
                newArr = cands[:i] + cands[i+1:]
                helper(newArr, cur + [e])

        helper(nums, [])
        return self.res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        At each index, select one from available
        """
        res = []

        def helper(cur, avail):
            if len(cur) == len(nums):
                res.append(cur)
                return

            for ind, a in enumerate(avail):
                helper(cur + [a], avail[:ind] + avail[ind+1:])
            

            
        for i in range(len(nums)):
            helper([nums[i]], nums[:i] + nums[i+1:])
        return res
