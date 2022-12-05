class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        """
        skill = [3,2,5,1,3,4]
        
        len(skill) = 6
        sum(skill) = 18
        
        numberOfGroups = len(skill) / 2 = 6/2 = 3
        
        sizePerGroup = sum(skill) / numberOfGroups = 18/3 = 6
        
        groups = []
        
        counter = {3:2, 2:1, 5:1, 1:1, 4:1}
        
        [3,2,5,1,3,4]
         i
        
        cur = skill[i] = 3
        if sizePerGroup - cur = 6 - 3 = 3 in counter:
            counter[cur] -= 1
        else:
            return -1
        if counter[cur] == 0:
            del counter[cur]
            
        groups.append((cur, sizePerGroup - cur))
        
        res = 0
        for i, j in groups:
            res += i*j
        return res / 2
        """
        totalSkill = sum(skill)
        numberOfGroups = len(skill) / 2
        sizePerGroup = totalSkill // numberOfGroups
        if totalSkill % numberOfGroups != 0:
            return -1
        groups = []
        
        counter = {}
        for sk in skill:
            counter[sk] = counter.get(sk, 0) + 1
        
        for i, cur in enumerate(skill):
            if sizePerGroup - cur in counter:
                counter[sizePerGroup - cur] -= 1
            else:
                return -1
            if counter[sizePerGroup - cur] == 0:
                del counter[sizePerGroup - cur]
            groups.append((cur, sizePerGroup-cur))
        res = 0
        for i, j in groups:
            res += i*j
        return int(res // 2)