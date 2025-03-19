class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        count = 0

        for i in range(n-2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                count += 1
        if nums[n-2] == 1 and nums[n-1] == 1:
            return count
        else:
            return -1


        