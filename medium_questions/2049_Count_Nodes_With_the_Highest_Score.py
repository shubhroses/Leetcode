class Node:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        """
        Removing each node we can figure out the size of the subtree to the left and to the right 
        Then can figure out above with total - left - right - 1
        for each node calculate = left * right * above
        add to dict 


        1. Create graph from parents
            for i, v in parents:
                adj:
                    -1 : [0]
                    2: [1, 3]
                    0: [2, 4]
        
        node
            val: 0
            left = 2
                left = 1
                right = 3
            right = 4
        """
        adj = collections.defaultdict(list)
        for i, v in enumerate(parents):
            adj[v].append(i)
        
        def returnTree(val):
            newNode = Node(val)
            children = adj[val]
            if children:
                newNode.left = returnTree(children[0])
                if len(children) == 2:
                    newNode.right = returnTree(children[1])
            return newNode
        
        root = returnTree(0)
        self.countToElements = collections.defaultdict(list)
        def getSubTreeSize(node):
            if not node:
                return 0
            left = getSubTreeSize(node.left)
            right = getSubTreeSize(node.right)
            self.countToElements[node.val] = (left, right)
            return left + right + 1
        getSubTreeSize(root)

        print(self.countToElements.items())
        scoreToNode = collections.defaultdict(list)
        nodeCount = len(parents)
        for node, (left, right) in self.countToElements.items():
            above = nodeCount - left - right - 1
            if left == 0:
                left = 1
            if right == 0:
                right = 1
            if above == 0:
                above = 1
            
            score = left * right * above
            scoreToNode[score].append(node)
        highestScore = max(scoreToNode.keys())
        return len(scoreToNode[highestScore])

