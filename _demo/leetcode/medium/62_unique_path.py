"""
dp
"""

class Solution:
    def uniquePaths(self, row: int, col: int) -> int:
        """
        Since only 2 options are possible, either from the cell above or left, it is a dp problem.
        """
        def is_valid(i, j):
            if i >= row or j >= col or i < 0 or j < 0:
                return False
            else:
                return True
        dp = [[0 for j in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                if i ==0 and j ==0:
                    dp[i][j] = 1
                if is_valid(i -1, j):
                    dp[i][j] += dp[i-1][j]
                if is_valid(i, j-1):
                    dp[i][j] += dp[i][j-1]
        return dp[row-1][col-1]
    
inp = (3,2)
s = Solution()
res = s.uniquePaths(*inp)
print(res)