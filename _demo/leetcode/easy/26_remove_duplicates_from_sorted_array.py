class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ix = 0
        for i in range(1, len(nums)):
            if nums[ix] != nums[i]:
                ix += 1
                nums[ix] = nums[i]
        return ix + 1