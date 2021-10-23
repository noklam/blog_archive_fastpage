#
# @lc app=leetcode id=1814 lang=python3
#
# [1814] Count Nice Pairs in an Array
#

# @lc code=start
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        """
        [42,11,1,97]
        [24,11,1,79]
        Diff List
        [18,0,0,18]
        """
        def rev(int_):
            return int(str(int_)[::-1])
        count = 0
        reverse_num = list(map(rev, nums))
        diff = [a-b for a,b in zip(nums, reverse_num)]
        counter = collections.Counter(diff)
        
        # Math Combination problems
        for k,v in counter.items():
            if v>=2:
                count = count + math.comb(v,2)
                count = count % (10**9 + 7 )
        return count 
                
        
# @lc code=end

