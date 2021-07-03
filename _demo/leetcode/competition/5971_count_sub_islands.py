"""
Copied Solution
dfs backtrack revisited
"""

class Solution(object):
    def countSubIslands(self, A, B):
        n, m = len(A), len(A[0])

        def dfs(i, j):
            B[i][j] = 0
            res = A[i][j]
            for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                x, y = i + di, j + dj
                if 0 <= x < n and 0 <= y < m and B[x][y] == 1:
                    res &= dfs(x, y)
            return res

        return sum(dfs(i, j) for i in xrange(n) for j in xrange(m) if B[i][j])