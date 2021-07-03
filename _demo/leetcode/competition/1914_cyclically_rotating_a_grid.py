"""
#medium #array
1. iterate layer
2. get corresponding index
"""


import numpy as np
class Solution:
    def rotateGrid(self, grid: List[List[int]], step: int) -> List[List[int]]:
        new_grid = grid.copy()
        row, col = len(grid), len(grid[0])
        n_layer = min(row//2, col//2)
        array_k = {}

        # Get Layer index
        for k in range(n_layer):
            i,j = k,k
            start_i, start_j = i, j
            array_k[k] = {}
            idx = 0
            tmp = []
            while True:
                "Get a list for layer k, also save the index"
                array_k[(i,j)] = (k, idx)
                tmp.append(grid[i][j])
                if i < row -1 -k and j == start_j:
                    i = i + 1
                elif i == row -1 -k and j < col -1 -k:
                    j = j + 1
                elif j == col -1 -k and i != k:
                    i = i -1
                elif i ==k and j >= start_j:
                    j = j -1

                idx += 1

                if i == start_i and j == start_j:
                    array_k[k]['l'] = tmp
                    break
        array_d = {}
        
        # Main
        for i in range(row):
            for j in range(col):
                r = row - k*2
                c = col - k*2
                max_n = r*2 + c*2
                new_k = k//max_n

                # Rotate
                layer, idx = array_k[(i,j)]
                new_list = array_k[layer]['l']
                new_idx = (idx - step) % len(new_list)
                # print(idx, step, new_idx,new_list[new_idx], i, j)
                new_grid[i][j] = new_list[new_idx]

        return new_grid

