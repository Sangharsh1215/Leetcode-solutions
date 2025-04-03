# Last updated: 4/3/2025, 10:16:12 PM
class Solution(object):
    def maximumTripletValue(self, nums):
        n = len(nums)
        res = 0
        maxdif = 0
        premax = nums[0]

        for k in range(1,n):
            res = max(res, maxdif*nums[k])
            premax = max(premax,nums[k])

            maxdif = max(maxdif,premax - nums[k])
        return res