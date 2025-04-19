# Last updated: 4/20/2025, 1:58:44 AM
from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n):
            left = bisect_left(nums, lower - nums[i], i + 1, n)
            right = bisect_right(nums, upper - nums[i], i + 1, n)
            count += right - left
        return count

        