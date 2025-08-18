# Last updated: 8/19/2025, 1:12:37 AM
class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        maxar = 0

        while l < r:
            w = r-l
            h = min(height[l],height[r])
            maxar = max(maxar,w*h)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxar


        