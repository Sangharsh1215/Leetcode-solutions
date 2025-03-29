# Last updated: 3/30/2025, 2:23:18 AM
class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)

        pos = [num for num in nums if num>0]
        neg = [num for num in nums if num<0]

        x = []
        i = 0

        while i < len (pos) and i < len(neg):
            x.append(pos[i])
            x.append(neg[i])
            i += 1

        return x


            