
def minimumDifference(nums):
    def helper(i, s1, s2):
        if i == len(nums):
            return abs(s1 - s2)
        dif1 = helper(i+1, s1 + nums[i], s2)
        dif2 = helper(i+1, s1, s2 + nums[i])
        
        return min(dif1, dif2)

    return helper(0, 0, 0)

if __name__ == "__main__":
    print(minimumDifference([1, 2, 3, 9]))
    print(minimumDifference([1, 2, 7, 1, 5]))
    print(minimumDifference([1, 3, 100, 4]))