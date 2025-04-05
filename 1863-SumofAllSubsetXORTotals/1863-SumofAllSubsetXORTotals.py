# Last updated: 4/5/2025, 7:27:59 PM
class Solution(object):
    def subsetXORSum(self, nums):
        res = 0

        for num in nums:
            res = res | num

        return res * 2**(len(nums)-1)

                
        