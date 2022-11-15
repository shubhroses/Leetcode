class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        graph = defaultdict(list)
        for u, t, w in sorted(zip(username, timestamp, website)):
            graph[u].append(w)
        
        counter = Counter()
        for u, routes in graph.items():
            for triple in set(itertools.combinations(routes, 3)):
                counter[triple]+=1
        
        pattern, count = None, 0
        for pat, c in counter.items():
            if c > count:
                pattern = pat
                count = c
            elif c == count and pattern > pat:
                pattern = pat
                
        return pattern
                




        """
        user: [(website, timestamp), (website, timestamp), (website, timestamp)]
        time stamps are in order
        
        iterate through array in jumps of size 3
        
        user: {(w1, w2, w3), ... } all patterns
        
        for each pattern, count how many users have that pattern
        
        {ua: [(a, 1), (b, 2), (a, 3)],
         ub: [(a, 4), (b, 5), (c, 6)]}
         
        {ua: {(a, b, a)},
         ub: {(a, b, c)}
         
        all pattern = {(a, b, a), (a, b, c)}
        
        pattern to count: {(a, b, a): 1, (a, b, c): 1}
        
        return pattern with max count in pattern to count 
        """
        triple = [(username[i], timestamp[i], website[i]) for i in range(len(username))]
        triple.sort(key=lambda x:x[1])
        
        print(triple)
        userToSite = collections.defaultdict(list)
        for t in triple:
            user = t[0]
            time = t[1]
            w = t[2]
            userToSite[user].append((w, time))
        userToPattern = collections.defaultdict(set)
        allPatterns = set()
        for user in userToSite.keys():
            test = userToSite[user]
            
            if len(test) < 3:
                continue
            
            #For the array we need every in order sub array of length 3
            for i in range(len(test)-2):
                for j in range(i+1, len(test)-1):
                    for k in range(j+1, len(test)):
                        pattern = (test[i][0], test[j][0], test[k][0])
                        userToPattern[user].add(pattern)
                        allPatterns.add(pattern)
        
        patternToCount = {}
        for pattern in allPatterns:
            count = 0
            for user in userToPattern.keys():
                if pattern in userToPattern[user]:
                    count += 1
            patternToCount[pattern] = count
        print(patternToCount)
        
        countToPattern = collections.defaultdict(list)
        for pattern, count in patternToCount.items():
            countToPattern[count].append(pattern)
            
        for count in countToPattern.keys():
            countToPattern[count].sort()
        
        return list(countToPattern[max(countToPattern)][0])
        """
        userToSite = {joe   : [(home, 1), (about, 2), (career, 3)], 
                      james : [(home, 4), (cart, 5), (maps, 6), (home, 7)], 
                      mary  : [(home, 8), (about, 9), (career, 10)]}
        
        userToPattern = {joe    : {(home, about, career)},
                         james  : {(home, cart, maps), (cart, maps, home)},
                         mary   : {(home, about, career)}}}
        allPatterns = {(home, about, career), (home, cart, maps),  (cart, maps, home)}
        
        patternToCount = {(home, about, career) : 2, 
                          (home, cart, maps) : 1,
                          (cart, maps, home): 1}
        return home about caree
        """