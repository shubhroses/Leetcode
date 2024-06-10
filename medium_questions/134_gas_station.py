class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Starting at every index in in range 0 to len(gas) - 1

        for i in range(len(gas)):
            iterate through 

            gasLeft = gas[i]
              for j in range(i, i + len(gas)):
                pos = j % len(gas)

                gasLeft = max(gasLeft - cost[pos], gas[pos])
                if gasLeft < cost[pos]:
                    break
                
        create a difference array
        maintain total and left
        iterate through difference array
        find first positive that lets us get to the end

 
        """
        if sum(gas) < sum(cost):
            return -1
        res = 0
        total = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                res = i + 1
        return res
