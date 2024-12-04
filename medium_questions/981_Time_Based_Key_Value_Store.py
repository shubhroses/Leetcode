class TimeMap:

    def __init__(self):
        self.map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # If the key does not exist, return an empty string
        if key not in self.map:
            return ""
        
        arr = self.map[key]
        l, r = 0, len(arr) - 1
        result = ""
        
        # Perform binary search
        while l <= r:
            m = (l + r) // 2
            if arr[m][1] <= timestamp:
                # Update result and move to the right to find the largest timestamp
                result = arr[m][0]
                l = m + 1
            else:
                # Move to the left
                r = m - 1

        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

"""
have a map (key, [value, timestamp]) where the list is sorted based on timestamp

on a set append to list

on a get 
    search list using binary search to find pair 
    where m[1] <= target and m+1[1] > target

    981_Time_Based_Key_Value_Store.py
"""
