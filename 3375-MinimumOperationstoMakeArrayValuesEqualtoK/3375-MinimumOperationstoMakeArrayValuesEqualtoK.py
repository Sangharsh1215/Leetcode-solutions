# Last updated: 4/9/2025, 10:09:22 PM
class Solution(object):
    def minOperations(self, nums, k):
        if min(nums) < k:
            return -1
        count = 0
        ans = set()

        for num in nums:
            ans.add(num)

        return len(ans)-1 if k in ans else len(ans)


        