from collections import deque

def can_construct(originalSeq, sequences):
    sortedOrder = []
    if len(originalSeq) <= 0:
        return False
    
    inDegree = {}
    graph = {}
    for sequence in sequences:
        for num in sequence:
            inDegree[num] = 0
            graph[num] = []

    for sequence in sequences:
        for i in range(1, len(sequence)):
            parent, child = sequence[i-1], sequence[i]
            graph[parent].append(child)
            inDegree[child] += 1
    if len(inDegree) != len(originalSeq):
        return False
    
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)
    
    while sources:
        if len(sources) > 1:
            return False
        if originalSeq[len(sortedOrder)] != sources[0]:
            return False
        
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)
    return len(sortedOrder) == len(originalSeq)

def main():
    print("Can construct: " + 
          str(can_construct([1,2,3,4], [[1,2], [2,3], [3,4]])))
    print("Can construct: " + 
          str(can_construct([1,2,3,4], [[1,2], [2,3], [2,4]])))
    print("Can construct: " + 
          str(can_construct([3,1,4,2,5], [[3,1,5], [1,4,2,5]])))
    
main()