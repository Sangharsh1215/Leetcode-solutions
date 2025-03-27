# Last updated: 3/27/2025, 10:33:21 PM
class Solution(object):
    def minimumIndex(self, nums):
        from collections import Counter

        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        total_count = nums.count(candidate)
        
        left_count = 0
        n = len(nums)
        
        for i in range(n - 1):  
            if nums[i] == candidate:
                left_count += 1
            
            left_size = i + 1
            right_size = n - left_size
            
            if left_count * 2 > left_size and (total_count - left_count) * 2 > right_size:
                return i
        
        return -1


            