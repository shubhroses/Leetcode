class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """
        Greedy Approach
        Sort by numberOfUnitxPerBox
        Keeps adding max
        
        [[1, 3],
         [2, 2],
         [3, 1]]
         
        TruckSize = 4
        
        
        """
        res = 0
        boxTypes.sort(key = lambda x: x[1], reverse = True)

        for arr in boxTypes:
            take = min(truckSize, arr[0])
            res += take*arr[1]
            
            truckSize -= take
            if truckSize == 0:
                break
        return res