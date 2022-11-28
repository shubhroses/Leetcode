class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        An ugly number is a positive integer whose prime factor is limited ot 2, 3, and 5. 
        Return the nth ugly number
        
        Brute force:
            Create a for loop
            Check if ugly number
                If it is, increment count
                if count == n:
                    return number
        """
        seen = {1, }
        nums = []
        heap = []
        heappush(heap, 1)

        for _ in range(1690):
            curr_ugly = heappop(heap)
            nums.append(curr_ugly)
            for i in [2, 3, 5]:
                new_ugly = curr_ugly * i
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heappush(heap, new_ugly)
        return nums[n-1]