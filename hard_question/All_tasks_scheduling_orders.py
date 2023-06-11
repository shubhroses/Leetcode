import collections

def print_orders(tasks, prerequisites):
    """
    Prerequisites: [0, 1], [1, 2]
    degree: Any time a course requires another course as a prerequisite increase its degree
    prereq: Key should be a prereq for each element in the value list 
    Perform DFS with sources 
    """
    degree = collections.defaultdict(int)
    prereq = collections.defaultdict(list)
    for node, pre in prerequisites:
        degree[node]+=1
        prereq[pre].append(node)

    sources = collections.deque()
    for key in degree:
        if degree[key] == 0:
            sources.append(key)

def print_all_topologial_sorts(graph, inDegree, sources, sortedOrder):
    if sources:
        for vertex in sources:
            sortedOrder.append(vertex)
            sourcesForNextCall = collections.deque(sources)
            sourcesForNextCall.remove(vertex)
            for child in graph[vertex]:
                inDegree[child]-=1
                if inDegree[child] == 0:
                    sourcesForNextCall.append(child)
            print_all_topologial_sorts(graph, inDegree, sourcesForNextCall, sortedOrder)
            sortedOrder.remove(vertex)
            for child in graph[vertex]:
                inDegree[child] += 1
    if len(sortedOrder) == len(inDegree):
        print(sortedOrder)


def main():
    print("Task Orders: ")
    print_orders(3, [[0, 1], [1, 2]])
    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])
    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])
main()