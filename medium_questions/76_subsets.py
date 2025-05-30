# Commit for Monday, June 2, 2025
# Added for backdated commit on 5/23/2025
# Added for backdated commit on 5/19/2025
# Commit for Tuesday, June 3, 2025
# Commit for Wednesday, June 4, 2025
# Commit for Thursday, June 5, 2025
# Commit for Friday, June 6, 2025
# Commit for Monday, May 26, 2025
# Commit for Tuesday, May 27, 2025
# Commit for Wednesday, May 28, 2025
# Commit for Thursday, May 29, 2025
# Commit for Friday, May 30, 2025
class Solution: 
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        At every index can take or leave element
        helper function were you pass in i
        can take or leave element at i
        if i == len(nums) add to res set


        [3, 4]
               i 
        []
            [4]
            []
        [3]
            [3, 4]
            [3]
        
        """
        self.res = []
        
        def helper(i, cur):
            if i == len(nums):
                self.res.append(cur)
                return
            # take
            newCur = []
            if not cur:
                newCur = [nums[i]]
            else:
                newCur = cur.append(nums[i])
            helper(i+1, newCur)
            #leave
            helper(i+1, cur)

        helper(0, [])
        return self.res

        """
        [1, 2]
         i

        i = 0
        cur = []
        res = []

            i = 1
            cur = [1]

                i = 2
                cur = [1, 2]

                    i = 3


                i = 2
                cur = [1]

                    i = 

            i = 1
            cur = []
                
                i = 2
                cur = [2]
                
                i = 2
                cur = []
        

        """