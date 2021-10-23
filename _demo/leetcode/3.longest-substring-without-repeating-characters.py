#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        n = len(s)
        left = 0
        right = 0
        k = 1

        while right + k <= n:

            sub_str = s[left : right + k]
            # If no repeat - expand window and record max_len
            if len(sub_str) == len(set(sub_str)):
                max_len = max(max_len, k)
                k = k + 1

            # If repeat - increment left
            else:
                if left == right:
                    left += 1
                    right += 1
                else:
                    left = left + 1
            # print('len',sub_str, k)
        return max_len


# @lc code=end

