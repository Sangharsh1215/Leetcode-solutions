# Last updated: 7/28/2025, 4:48:27 PM
class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        sum = 0
        maxi = float('-inf')

        for i in range(n):
            sum = sum + nums[i]
            if sum > maxi:
                maxi = sum
            if sum < 0:
                sum = 0
        return maxi
        