import collections

def topological_sort(vertices, edges):
    # Result str
    sortedOrder = []
    if vertices <= 0:
        return sortedOrder

    # Indegree and adj list
    inDegree = {i:0 for i in range(vertices)}
    graph = {i:[] for i in range(vertices)}

    # Build graphs
    for parent, child in edges:
        graph[parent].append(child)
        inDegree[child] += 1

    # Put all sources in a queue
    sources = collections.deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    # Do bfs
    while sources:
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:
            inDegree[child]-=1
            if inDegree[child] == 0:
                sources.append(child)
    
    if len(sortedOrder) != vertices:
        return []
    
    return sortedOrder

def main() :
    print("Topological sort: " + str (topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " + str (topological_sort(5, [[4, 2], [4, 1], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +str (topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))

main ()
