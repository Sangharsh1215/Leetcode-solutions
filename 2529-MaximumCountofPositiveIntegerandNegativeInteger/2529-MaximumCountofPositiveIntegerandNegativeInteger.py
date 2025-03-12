class Solution(object):
    def maximumCount(self, nums):
        n = len(nums)
        countneg = 0
        countpos = 0
        
        for i in range(n):
            if nums[i] < 0:
                countneg += 1
            if nums[i] == 0:
                continue
            if nums[i] >= 0:
                countpos += 1

        return max(countneg,countpos) 
