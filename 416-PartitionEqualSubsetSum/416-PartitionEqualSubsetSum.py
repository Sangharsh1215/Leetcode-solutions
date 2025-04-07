# Last updated: 4/8/2025, 12:16:58 AM
class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2:
            return False
        n = len(nums)
        target = total//2
        dp = set()
        dp.add(0)

        for i in range(n-1,-1,-1):
            nextdp = set()
            for t in dp:
                nextdp.add(t+nums[i])
                nextdp.add(t)

            dp = nextdp

        return True if target in dp else False


            
        
        