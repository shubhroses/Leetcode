import heapq
def find_Kth_smallest(lists, k):
    """
    
    """
    minHeap = []
    for i in range(len(lists)):
        heapq.heappush(minHeap, [lists[i][0], 0, lists[i]])

    numberCount, number = 0, 0

    while minHeap:
        number, i, list = heapq.heappop(minHeap)
        numberCount += 1
        if numberCount == k:
            break
        if len(list) > i + 1:
            heapq.heappush(minHeap, [list[i+1], i+1, list])
        
    return number
        

if __name__ == "__main__":
    print("Kth smallest number is: " + str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))
