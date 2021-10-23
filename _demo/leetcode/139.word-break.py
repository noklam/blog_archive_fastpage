from typing import *
#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ...
# @lc code=end

s = "leetcode"
wordDict = ["leet","code"]
# s = "applepenapple"
# wordDict = ["apple","pen"]
# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]

sol = Solution()
print(sol.wordBreak(s, wordDict))
print(1)