class Solution:
    def knightDialer(self, n: int) -> int:
        
        if n == 1:
            return 10
        
#         init = {
# Note there is no key = 5, because once n >= 2, we go anywhere if we start with 5, so it is not an option
# E.g. 0 can come from 4 or 6
#             0: [4, 6],
#             1: [6, 8],
#             2: [7, 9],
#             3: [4, 8],
#             4: [0, 3, 9],
#             6: [0, 1, 7],
#             7: [2, 6],
#             8: [1, 3],
#             9: [2, 4]
#         }
        
        list1 = [1,1,1,1,1,0,1,1,1,1]
        list2 = [0,0,0,0,0,0,0,0,0,0]
        for i in range(n - 1):
		# Just follow the init logic
            list2[0] = list1[4] + list1[6]
            list2[1] = list1[6] + list1[8]
            list2[2] = list1[7] + list1[9]
            list2[3] = list1[4] + list1[8]
            list2[4] = list1[0] + list1[3] + list1[9]
            list2[6] = list1[0] + list1[1] + list1[7]
            list2[7] = list1[2] + list1[6]
            list2[8] = list1[1] + list1[3]
            list2[9] = list1[2] + list1[4]
            list1 = list2[:]
        
        return sum(list2) % (1000000007)
        """
        { 1: [8, 6],
          2: [7, 9],
          3: [4, 8], 
          4: [3, 9, 0],
          5: [],
          6: [7, 0, 1],
          7: [2, 6],
          8: [1, 3],
          9: [4, 3],
          0: [4, 6]}
          
        Starting at each button get count 
        """
        adj = { 1: [8, 6],
          2: [7, 9],
          3: [4, 8], 
          4: [3, 9, 0],
          5: [],
          6: [7, 0, 1],
          7: [2, 6],
          8: [1, 3],
          9: [4, 3],
          0: [4, 6]}
        
        visited = {}
        def helper(count, button):
            if count >= n:
                return 1
            if (count, button) in visited:
                return visited[(count, button)]
            nextButton = adj[button]
            res = 0
            for b in nextButton:
                res += helper(count+1, b)
            visited[(count, button)] = res
            return res
            
        result = 0

        for i in range(10):
            result += helper(1, i)
        return result%(10**9 + 7)
        """
        count = 1
        button = 1
        """
        