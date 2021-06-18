class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_nums = []
        zero_array = []
        for idx,  num in enumerate(nums):
            if num == 0:
                zero_array.append(num)
            else:
                new_nums.append(num)
                
        return new_nums + zero_array
        
        
class Solution:
    def moveZeroes(self, nums):
        """
Do not return anything, modify nums in-place instead.
        """
        pos = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                print('Before: ', nums)
                nums[pos], nums[i] = nums[i], nums[pos]
                print('After: ', nums, "\n")
                pos += 1