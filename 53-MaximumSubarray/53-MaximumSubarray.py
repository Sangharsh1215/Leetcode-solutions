# Last updated: 7/28/2025, 4:47:44 PM
class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        sum = 0 
        max = float('-inf')
        for i in range(n):
            sum = sum + nums[i]

            if sum > max:
                max = sum
            if sum < 0:
                sum = 0


        
        return max
        