# Last updated: 4/4/2025, 6:43:18 PM
class Solution(object):
    def trap(self, height):
        x = max(height)
        i = height.index(x)
        maxi = 0
        wb = 0
        res = 0
        n = len(height)

        for j in range(1,i+1):
            if height[j] >= height[maxi]:
                res += wb
                wb = 0
                maxi = j
            wb += (height[maxi] - height[j])

        maxi = n-1
        wb = 0


        for k in range(n-2,i-1,-1):
            if height[k] >= height[maxi]:
                res += wb
                wb = 0
                maxi = k
            wb += (height[maxi] - height[k])

        return res 


        