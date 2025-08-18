# Last updated: 8/18/2025, 11:36:46 PM
class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        mp = {}
        for i,num in enumerate(nums):
            comp = target - num
            if comp in mp:
                return (mp[comp],i)
            mp[num] = i
        