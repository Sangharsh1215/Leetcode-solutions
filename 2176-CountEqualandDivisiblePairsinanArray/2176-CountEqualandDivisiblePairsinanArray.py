# Last updated: 4/17/2025, 9:51:49 PM
class Solution(object):
    def countPairs(self, nums, k):
        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    res += 1
        return res

        