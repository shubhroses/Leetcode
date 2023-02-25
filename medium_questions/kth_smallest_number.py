import heapq

def kthSmallest(arr, N, K):
 
    heap = []
    heapq.heapify(heap)

    for num in arr:
        heapq.heappush(heap, -1*num)
        while len(heap) > K:
            heapq.heappop(heap)

    return -1*heap[0]
 
 
# Driver code
if __name__ == '__main__':
    arr = [3,2,1,5,6,4]
    N = len(arr)
    K = 2
 
    # Function call
    print("K'th smallest element is", kthSmallest(arr, N, K))