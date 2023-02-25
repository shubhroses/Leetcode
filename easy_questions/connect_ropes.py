import heapq
 
def minCost(ropeLengths):
    heap = ropeLengths
    heapq.heapify(heap)

    res = 0
    while len(heap) > 1:
        top = heapq.heappop(heap)
        next = heapq.heappop(heap)
        res += top + next
        heapq.heappush(heap, top + next)
    return res
 
 
# Driver code
if __name__ == '__main__':
    print("Total cost for connecting ropes is " + str(minCost([1, 3, 11, 5])))
    print("Total cost for connecting ropes is " + str(minCost([3, 4, 5, 6])))
    print("Total cost for connecting ropes is " + str(minCost([1, 3, 11, 5, 2])))
 
# This code is contributed by shivampatel5