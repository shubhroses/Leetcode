# Commit for Monday, May 26, 2025
# Added for backdated commit on 5/23/2025
# Added for backdated commit on 5/19/2025
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
                self.res.append(cur[:])  # Make a copy of cur
                return
            # take
            cur.append(nums[i])
            helper(i+1, cur)
            cur.pop()  # Remove the last element
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