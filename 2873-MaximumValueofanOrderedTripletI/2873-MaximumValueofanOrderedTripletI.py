# Last updated: 4/2/2025, 9:53:00 PM
class Solution(object):
    def maximumTripletValue(self, nums):

        n = len(nums)
        left = nums[0]
        res = 0

        for j in range(1,n):
            if nums[j] > left:
                left = nums[j]
                continue
            for k in range(j+1,n):
                res = max(res,(left - nums[j]) * nums[k])
        return res
                


        
        