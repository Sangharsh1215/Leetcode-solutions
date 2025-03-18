class Solution(object):
    def longestNiceSubarray(self, nums):
        maxlen = 0
        bitmask = 0 
        left = 0

        for right in range(len(nums)):
            while (bitmask & nums[right]) != 0:
                bitmask ^= nums[left]
                left += 1

            bitmask |= nums[right]

            maxlen = max(maxlen, right-left+1)

        return maxlen


        