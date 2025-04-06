# Last updated: 4/6/2025, 4:02:46 PM
class Solution(object):
    def largestDivisibleSubset(self, nums):
        nums.sort()
        n = len(nums)
        cache = {}

        def dfs(i):
            if i == n:
                return []
            if i in cache:
                return cache[i]
            res = [nums[i]]
            for j in range(i+1,n):
                if nums[j] % nums[i] == 0:
                    temp = [nums[i]] + dfs(j)
                    if len(temp) > len(res):
                        res = temp
                cache[i] = res
            return res

        res = []
        for i in range(n):
            tmp = dfs(i)
            if len(tmp) > len(res):
                res = tmp

        return res