class Solution(object):
    def maximumCandies(self, candies, k):

        n = len(candies)
        if sum(candies) < k:
            return 0
        l = 1
        r = max(candies)
        best = 0
        while l <= r:
            mid = (l + r)//2

            count = sum(num//mid for num in candies)

            if count < k:
                r = mid -1
            else:
                best = mid
                l = mid + 1

        return best