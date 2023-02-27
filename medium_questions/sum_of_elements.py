from heapq import *

def find_sum_of_elements(nums, k1, k2):
    minHeap = []

    for num in nums:
        heappush(minHeap, num)
    
    for _ in range(k1):
        heappop(minHeap)
    
    elementSum = 0

    for _ in range(k2-k1-1):
        elementSum += heappop(minHeap)
    
    return elementSum

if __name__ == "__main__":
    print("Sum of all numbers between k1 and k2 smallest numbers: " + str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " + str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))
