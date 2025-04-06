# Last updated: 4/7/2025, 12:16:35 AM
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        l = []
        dq = deque()
        for i in range(n):
            if dq and dq[0] <= (i-k):
                dq.popleft()
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop() 
            dq.append(i)

            if (i>=(k-1)):
                l.append(nums[dq[0]])

        return l




        