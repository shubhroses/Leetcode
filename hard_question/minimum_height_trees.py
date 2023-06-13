import collections

# def find_trees(nodes, edges):
#     """
#     Perform BFS maintaining height 
#     If height == min: return all 
#     """
#     depthNodes = collections.defaultdict(list)
#     justNodes = set()

#     adj = collections.defaultdict(list)
#     for e1, e2 in edges:
#         justNodes.add(e1)
#         justNodes.add(e2)
#         adj[e1].append(e2)
#         adj[e2].append(e1)

#     def helper(root):
#         level = 1
#         sources = collections.deque([root])
#         visited = set([root])
#         while sources:
#             for _ in range(len(sources)):
#                 top = sources.popleft()
#                 for neigh in adj[top]:
#                     if neigh in visited:        
#                         continue
#                     visited.add(neigh)
#                     sources.append(neigh)
#             level += 1
#         return level

#     for node in justNodes:
#         depthNodes[helper(node)].append(node)
    
#     mn = min(depthNodes.keys())
#     return depthNodes[mn]

def find_trees(nodes, edges):
    """
    Keep taking off leafs until only left with 1 or 2 nodes 
    A leaf only has 1 edge connected to it
    """
    inDegree = {i:0 for i in range(nodes)}
    graph = {i:[] for i in range(nodes)}

    for n1, n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)

        inDegree[n1] += 1
        inDegree[n2] += 1

    leaves = collections.deque()
    for node, degree in inDegree.items():
        if degree == 1:
            leaves.append(node)

    totalNodes = nodes
    while totalNodes > 2:
        leavesSize = len(leaves)
        totalNodes -= leavesSize
        for i in range(0, leavesSize):
            vertex = leaves.popleft()
            for child in graph[vertex]:
                inDegree[child]-=1
                if inDegree[child] == 1:
                    leaves.append(child)
    return list(leaves)
    
    pass


def main():
    print("Roots of MSTs: " +
          str(find_trees(5, [[0,1], [1, 2], [1, 3], [2, 4]])))
    print("Roots of MSTs: " +
          str(find_trees(4, [[0,1], [0, 2], [2, 3]])))
    print("Roots of MSTs: " +
          str(find_trees(4, [[1, 2], [2, 3]])))
    

main()