class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        if not grid1 or not grid2:
            return 0
        import numpy as np
        global res
        res = 0
        grid1 = np.array(grid1)
        grid2 = np.array(grid2)
        to_visit = grid2.copy()        
        row, col = grid2.shape
        
        def is_boundary(i, j):
            if i >= row or j >= col or i<0 or j <0:
                return True
            else:
                return False
        
        # # We only need to visit the 1 in grid2, we don't care about the 0s.
        # list_to_visit = list(map(tuple,  np.where(to_visit)))
        # list_to_visit = list(zip(*list_to_visit))
        
        def _dfs( grid, i, j, b=True):
            if is_boundary(i,j):
                return True
            
            if grid[i][j] == 1 :
                grid[i][j] = 0
                if grid1[i][j] == 1:
                    b1= _dfs(grid, i, j-1)
                    b2= _dfs(grid, i, j+1)
                    b3= _dfs(grid, i-1, j)
                    b4= _dfs(grid, i+1, j)
                    return b1 and b2 and b3 and b4
                    # print('Fail', i,j)
                    # return True
                else:
                    print('Fail', i,j)
                    return False # Not subisland
        
        # Backtrack
        for i in range(row):
            for j in range(col):
                if _dfs(to_visit, i, j):
                    res += 1
        return res

                
            
            
        