class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        """
        If the number of distinct chars in each string is equal:
            True
        If the number of distinct chars in each string differs by 1
            if len(word1) == #distinct chars word1:
                False
            elif len(word2) == # distinct chars word2:
                False
            else:
                True
        if number of distinct chars in string differ by 2:
            if distinct chars in word1 == 1 and min(count chars in word2) == 1:
                return True
            if distinct chars in word2 == 1 and min(count chars in word1) == 1:
                return True
        return false
        
        
        #possible
        abc
        dee        
        
        abe
        dec
        
        # not possibke
        abc 
        de
        
        # not possible
        abcc
        ac
        
        accc
        ab
        
        Maybe has to do with the number of characters that exist in both word1 and wod2
        
            
        aaab
         
        # differ by 1
        abccc = 3 {a:1, b:1, c:3}
        de = 1 {d:1, e:1}
        
        
        # differ by 2 
        aabc = 3 
        aa = 1
          
        aaba = 2
        ac = 2 
         
        aabbcc
        aa
        
        a
        bb
        """
        
        counter1 = defaultdict(int)
        for char in word1:
            counter1[char] += 1
            
        counter2 = defaultdict(int)
        for char in word2:
            counter2[char] += 1
            
        
        print(counter1)
        print(counter2)
        for i in 'abcdefghijklmnopqrstuvwxyz': #1 
            for j in 'abcdefghijklmnopqrstuvwxyz': #2
                if counter1[i] == 0 or counter2[j] == 0: 
                    continue
                # counter1 will decrement one i, counter2 will increment one i
                counter1[i] -= 1
                counter2[i] += 1
                
                
                # counter2 will decrement one j, counter1 will increment one jd
                counter2[j] -=1
                counter1[j] +=1
                
                # Check if both counters are equal
                distinct1 = sum([1 for key in counter1.keys() if counter1[key] != 0])
                distinct2 = sum([1 for key in counter2.keys() if counter2[key] != 0])
                print(i, j)
                if distinct1 == distinct2:
                    return True
                
                # counter1 will decrement one i, counter2 will increment one i
                counter1[i] += 1
                counter2[i] -= 1
                
                
                # counter2 will decrement one j, counter1 will increment one jd
                counter2[j] +=1
                counter1[j] -=1
                print(counter1)
                print(counter2)
        return False