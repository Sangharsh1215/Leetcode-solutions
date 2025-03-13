class Solution(object):
    def minZeroArray(self, nums, queries):
        n = len(nums)
        diff = [0] * (n + 1)
        sum_val = 0
        pos = 0
        
        for i in range(n):
            while sum_val + diff[i] < nums[i]:
                if pos == len(queries):  
                    return -1
                
                start, end, val = queries[pos]
                pos += 1
                
                if end < i:  
                    continue

                diff[max(start, i)] += val
                if end + 1 < n:
                    diff[end + 1] -= val
            
            sum_val += diff[i]
        
        return pos