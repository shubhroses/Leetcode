import random
class RandomizedSet:

    def __init__(self):
        self.s = set()

    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        self.s.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.s:
            self.s.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.sample(self.s, 1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

class RandomizedSet:

    def __init__(self):
        self.savedMap = {}
        self.savedList = []

    def insert(self, val: int) -> bool:
        if val in self.savedMap:
            return False
        self.savedMap[val] = len(self.savedList)
        self.savedList.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.savedMap:
            return False
        lastElement = self.savedList[-1] # Get last element in list
        ind = self.savedMap[val]    # Get index of val to be deleted
        self.savedList[ind] = lastElement # put last element in list at index to be deleted
        self.savedMap[lastElement] = ind # Save the new location of last element 
        
        self.savedList.pop()
        del self.savedMap[val]
        return True
    
    """
    1. 
    map = {a:0, b:1, c:2}
    savedList = [a, b, c]
    
    2. 
    val = a
    lastElement = c
    ind = map[a] = 1
    saveList = [c, b, c]
    map = {a:0, b:1, c:0}
    
    3. 
    saveList = [c, b]
    map = {b:1, c:0}
    
    """


    def getRandom(self) -> int:
        return random.choice(self.savedList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()