#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
from typing import List
# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        min_ = 2**31
        cumsum = nums[0]
        while l <= r and r < len(nums):
            print(min_, l, r, nums[l:r+1])
            if cumsum < target:
                r = r + 1
                if r >= len(nums): break
                cumsum = cumsum + nums[r]
            else:
                min_ = min(min_, r - l + 1)
                cumsum = cumsum - nums[l]
                l = l + 1
                if l > r:
                    r = r + 1
                    if r >= len(nums): break
                    cumsum = cumsum + nums[r]
        return min_
            
s = Solution()
# nums = [2,3,1,2,4,3]
# target = 7
# print(s.minSubArrayLen(target, nums))

target = 4
nums = [1,4,4]
print(s.minSubArrayLen(target, nums))
        
# @lc code=end

