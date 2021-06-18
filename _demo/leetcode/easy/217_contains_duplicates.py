class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        n_set = len(set(nums))
        
        if n > n_set:
            return True
        else:
            return False