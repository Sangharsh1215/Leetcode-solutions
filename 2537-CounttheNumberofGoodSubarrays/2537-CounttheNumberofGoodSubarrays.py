# Last updated: 4/17/2025, 9:51:14 PM
from collections import defaultdict
class Solution(object):
    def countGood(self, nums, k):
        count = defaultdict(int)
        left = res = pair_count = 0

        for right in range(len(nums)):
            pair_count += count[nums[right]]
            count[nums[right]] += 1

            while pair_count >= k:
                res += len(nums) - right
                count[nums[left]] -= 1
                pair_count -= count[nums[left]]
                left += 1

        return res

            