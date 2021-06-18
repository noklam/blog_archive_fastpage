class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else: 
                d[num] = d[num] + 1
        for k,v in d.items():
            if v == 1:
                return k
            