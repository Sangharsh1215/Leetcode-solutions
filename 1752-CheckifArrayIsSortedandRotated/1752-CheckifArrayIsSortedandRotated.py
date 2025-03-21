// Last updated: 3/21/2025, 2:10:57 PM
class Solution(object):
    def check(self, nums):
        count = 0
        n = len(nums)    
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]: 
                count += 1
                if count > 1:
                    return False
                    
        return True
        