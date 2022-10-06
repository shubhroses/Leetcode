class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
        mat1map = {}
        mat2map = {}
        
        for r in range(len(mat1)):
            for c in range(len(mat1[0])):
                if mat1[r][c] == 0:
                    continue
                if r in mat1map:
                    mat1map[r][c] = mat1[r][c]
                else:
                    mat1map[r] = {c:mat1[r][c]}
        
        for r in range(len(mat2)):
            for c in range(len(mat2[0])):
                if mat2[r][c] == 0:
                    continue
                if c in mat2map:
                    mat2map[c][r] = mat2[r][c]
                else:
                    mat2map[c] = {r:mat2[r][c]}
                    
        """
        mat1map = {0: {0:1},
                   1: {0:-1, 2:3}}
                   
        mat2map = {0: {0:7},
                   2: {2:1}}
        
        m = 2
        n = 3
        
        res = [[0,0,0],
               [0,0,0]]
        r = 0
        c = 0
        
        row = {0:1}
        col = {0:7}
        res = 7
        
        key = 0
        
        """            
        
        def getVal(r, c):
            #multiply row r in mat1 with col c in mat2
            row = mat1map.get(r, {})
            col = mat2map.get(c, {})
            # r = 0, col = 0
            # row = {0:1}
            # col = {0:7}
            res = 0
            for key in row.keys():
                if key in col:
                    res += row[key] * col[key]
            return res
        
        m = len(mat1)
        n = len(mat2[0])
        res = []
        
        for r in range(m):
            cur = []
            for c in range(n):
                cur.append(getVal(r, c))
            res.append(cur)  
        return res
         
        """
        mat1 m x k   mat2 k x n
             r   c        r   c
             
        for row i in mat1 and col j in mat2 
        each index times each index added together
        
        mat1
        {row:{i:v}}
        
        {0: {0:1}
         1: {0:-1, 2:3}}
         
        mat2
        {col:{j:v}}
        
        {0: {0:7},
         1: {},
         2: {2:1}}
         
        m * n
        r   c
        res = [[0,0,0],[0,0,0]] 
        
        def getVal(r, c):
            #multiply row r in mat1 with col c in mat2
            row = mat1map[r]
            col = mat2map[c]
            # r = 0, col = 0
            # row = {0:1}
            # col = {0:7}
            res = 0
            for key in range(row.keys()):
                if key in col:
                    res += row[key] * col[key]
            return res

        for r in range(len(res)):
            for c in range(len(res[0])):
                res[r][c] = 
        """