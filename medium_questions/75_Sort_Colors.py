class Solution:
    def sortColors(self, arr: List[int]) -> None:
        
        
        
        
        
        """
        All elements < low are 0, and all elements > high are 2
        all elements from >= low < i are 1
        """
        low, high = 0, len(arr)-1
        i = 0
        while (i <= high):
            if arr[i] == 0:
                arr[i], arr[low] = arr[low], arr[i]
                i+=1
                low+=1
            elif arr[i] == 1:
                i+=1
            else:
                arr[i], arr[high] = arr[high], arr[i]
                high -=1