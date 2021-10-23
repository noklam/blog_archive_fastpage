#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r*r > x:
                r = int(r - (r*r - x)/(2*r))  # newton's method
        return r
# @lc code=end

