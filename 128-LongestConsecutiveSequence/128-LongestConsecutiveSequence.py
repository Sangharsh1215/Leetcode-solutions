# Last updated: 8/18/2025, 11:27:01 PM
class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums = list(set(nums))
        n = len(nums)
        nums.sort()
        maxi = 1
        count = 1

        for i in range(1,n):
            if nums[i] == nums[i-1] + 1:
                count += 1
            else:
                count = 1
            maxi = max(maxi,count)

        return maxi 




        