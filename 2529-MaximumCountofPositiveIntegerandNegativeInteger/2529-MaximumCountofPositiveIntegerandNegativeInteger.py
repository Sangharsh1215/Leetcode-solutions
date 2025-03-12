// Last updated: 3/12/2025, 4:47:05 PM
class Solution(object):
    def maximumCount(self, nums):
        n = len(nums)
        left = 0
        right = n

        while left < right:
            mid = (left + right)//2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid
        neg = left

        left = 0 
        right = n

        while left < right:
            mid = (left + right)//2
            if nums[mid] <= 0:
                left = mid + 1
            else:
                right = mid
        pos = n - left


        return max(pos, neg) 
