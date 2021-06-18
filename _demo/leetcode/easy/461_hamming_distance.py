class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Avoid using bin() since it turns this question to string manipulation question.
        ans = []
        while x or y:
          ans.append((x % 2) != (y % 2))
          x //= 2
          y //= 2
        return sum(ans)


"""
1 1 0 0
0 1 1 0
"""