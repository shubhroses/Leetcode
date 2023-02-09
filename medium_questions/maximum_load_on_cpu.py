def find_max_cpu_loads(jobs):
    jobs.sort(key = lambda x:x[0])
    
    cur = jobs[0][2]
    res = jobs[0][2]
    # print("jobs", jobs)

    heap = [(jobs[0][1], jobs[0][2])]

    heapq.heapify(heap)
    # print("heap :", heap)
    # print("cur: ", cur)
    
    for s, e, l in jobs[1:]:
        while heap and s > heap[0][0]:
            end, load = heapq.heappop(heap)
            cur -= load
        heapq.heappush(heap, (e, l))
        cur += l
        # print("heap: ", heap)
        # print("cur: ", cur)
        res = max(res, cur)
        
    return res


print(find_max_cpu_loads([[1,4,3], [2,5,4], [7,9,6]]))
print(find_max_cpu_loads([[6,7,10], [2,4,11], [8,12,15]]))
print(find_max_cpu_loads([[1,4,2], [2,4,1], [3,6,5]]))