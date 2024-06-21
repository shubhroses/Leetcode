class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        w -> e -> r -> t -> f
        
        Iterate through words in pairs
        find first letter that is differet and add to graph
        
        How should I create the graph?
            Use a linked list
            Create a adjacnecy list?
            
        If there is a cycle return ""
        
        1. Create adjacency list and a counter for the indegree of each word
        2. For each pair of adjacent words add to adj_list and counter
        3. Repeatedily pick off nodes with indegree of zero
        4. If not all letters are in putput there is a cycle
        Why is it that if all letters are not in the output then there is a cycle. If you continououly pop elements with an indegree of zero in a tree, you will eventually have no nodes left. In a graph with a cycle there will be nodes that have indegrees > 0 forever 
        """
        adj_list = collections.defaultdict(set)
        in_degree = collections.Counter({c:0 for word in words for c in word})
        # {a:0, b:0 ...}
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] +=1
                    break
            else:
                if len(second_word) < len(first_word):
                    return ""
        
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -=1
                if in_degree[d] == 0:
                    queue.append(d)
        
        if len(output) < len(in_degree):
            return ""
        
        return "".join(output)


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}  # {char: bool} False visited, True current path
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)
