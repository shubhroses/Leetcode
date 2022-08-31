import random
class Solution:

    def __init__(self, nums: List[int]):
        self.saved = nums
        #print(f"saved: {self.saved}")

    def reset(self) -> List[int]:
        #print(f"saved: {self.saved}")
        return self.saved

    def shuffle(self) -> List[int]:
        #print(f"saved: {self.saved}")
        ans = self.saved[:]                     # copy list
        for i in range(len(ans)-1, 0, -1):     # start from end
            j = random.randrange(0, i+1)    # generate random index 
            ans[i], ans[j] = ans[j], ans[i]    # swap
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()