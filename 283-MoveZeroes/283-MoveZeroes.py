# Last updated: 3/27/2025, 2:29:00 AM
class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        index = 0 

        for i in range(n):
            if nums[i] != 0:
                nums[i],nums[index] = nums[index],nums[i]
                index += 1
        return nums
        