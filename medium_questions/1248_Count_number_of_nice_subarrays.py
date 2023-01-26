class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        low_bound, index_of_left_most_odd_in_win, ans = -1, 0, 0
        for num in nums:
            k -= num % 2
            if nums[index_of_left_most_odd_in_win] % 2 == 0:
                index_of_left_most_odd_in_win += 1
            if k < 0:
                low_bound = index_of_left_most_odd_in_win
            while k < 0:    
                index_of_left_most_odd_in_win += 1
                k += nums[index_of_left_most_odd_in_win] % 2
            if k == 0:
                ans += index_of_left_most_odd_in_win - low_bound
        return ans

        dic = {0:1}
        count = 0
        res = 0

        for ind, num in enumerate(nums):

            print(f"num: {num}, dic: {dic}, res:{res}")
            if num % 2 == 1:
                count += 1

            if count - k in dic:
                res += dic[count - k]
            
            dic[count] = dic.get(count, 0) + 1

        print(res)
        return res