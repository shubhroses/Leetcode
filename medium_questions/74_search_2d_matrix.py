class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        1. Find the row that the target is in 
            Find the first row where starting element larger than target then search in row - 1 
        2. Do binary search in that row

        target = 30
                       m
        matrix = [[1],[10],[23]]
                   t         b
         
        candidateRow = -1
        """
        # t, b = 0, len(matrix)-1

        # candidateRow = 0

        # while t <= b:
        #     m = (t + b)//2
        #     if matrix[m][0] < target:
        #         t = m + 1
        #     elif matrix[m][0] > target:
        #         if m > 0 and matrix[m-1][0] < target:
        #             candidateRow = m-1
        #             break
        #         b = m - 1
        #     else:
        #         candidateRow = m
        #         break
        candidateRow = 0

        for i in range(len(matrix)):
            if matrix[i][0] > target:
                candidateRow = i - 1
                break
            elif matrix[i][0] == target:
                candidateRow = i
            elif i == len(matrix)-1:
                candidateRow = i
        candidateRow  = max(candidateRow, 0)
            
        print(candidateRow)
        l, r = 0, len(matrix[0])-1
        while l <= r:
            m = (l+r)//2
            if matrix[candidateRow][m] < target:
                l = m + 1
            elif matrix[candidateRow][m] > target:
                r = m - 1
            else:
                return True
        return False
