# Last updated: 4/9/2025, 4:03:08 AM
class Solution(object):
    def minimumOperations(self, nums):
        operations = 0
        while len(nums) != len(set(nums)):
            nums = nums[3:]
            operations += 1
        return operations






        