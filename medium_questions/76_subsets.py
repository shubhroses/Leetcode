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