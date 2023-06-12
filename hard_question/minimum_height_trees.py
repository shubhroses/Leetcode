import collections

def find_trees(nodes, edges):
    """
    Perform BFS maintaining height 
    If height == min: return all 
    """
    depthNodes = collections.defaultdict(list)
    justNodes = set()

    adj = collections.defaultdict(list)
    for e1, e2 in edges:
        justNodes.add(e1)
        justNodes.add(e2)
        adj[e1].append(e2)
        adj[e2].append(e1)

    def helper(root):
        level = 1
        sources = collections.deque([root])
        visited = set([root])
        while sources:
            for _ in range(len(sources)):
                top = sources.popleft()
                for neigh in adj[top]:
                    if neigh in visited:        
                        continue
                    visited.add(neigh)
                    sources.append(neigh)
            level += 1
        return level

    for node in justNodes:
        depthNodes[helper(node)].append(node)
    
    mn = min(depthNodes.keys())
    return depthNodes[mn]

def main():
    print("Roots of MSTs: " +
          str(find_trees(5, [[0,1], [1, 2], [1, 3], [2, 4]])))
    print("Roots of MSTs: " +
          str(find_trees(4, [[0,1], [0, 2], [2, 3]])))
    print("Roots of MSTs: " +
          str(find_trees(4, [[1, 2], [2, 3]])))
    

main()