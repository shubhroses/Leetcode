class TimeMap:

    def __init__(self):
        self.savedDict = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.savedDict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.savedDict:
            allVals = self.savedDict[key]
            if not allVals or timestamp < allVals[0][0]:
                return ""

            "Find first element with value lower than target"
            l, r = 0, len(allVals) - 1
            while l <= r:
                m = (l + r) // 2
                if allVals[m][0] <= timestamp:
                    if m == len(allVals)-1:
                        return allVals[m][1]
                    if allVals[m+1][0] > timestamp:
                        return allVals[m][1]
                    l = m + 1
                else:
                    r = m - 1
            
        else:
            return "" 


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)