// Last updated: 3/22/2025, 5:50:16 PM
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxi = float('-inf')
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                maxi = max(maxi,count)
                count = 0

        return max(maxi,count)

        