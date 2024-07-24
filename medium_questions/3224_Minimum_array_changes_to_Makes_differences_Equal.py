class Solution:
    def minChanges(self, nums, k):
        n = len(nums)             
        change_count = [0] * (k + 2)  
        change_count[0] = n // 2

        for i in range(n // 2):
            left = nums[i]
            right = nums[n - i - 1]
            cur_diff = abs(left - right)
            max_diff = max(left, right, k - left, k - right)
            
            change_count[cur_diff] -= 1
            change_count[cur_diff + 1] += 1
            change_count[max_diff + 1] += 1

        cur_changes = 0
        min_changes = n // 2
        for i in range(k + 1):
            cur_changes += change_count[i]
            min_changes = min(min_changes, cur_changes)

        return min_changes
