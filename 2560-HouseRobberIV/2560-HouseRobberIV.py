class Solution(object):
    def minCapability(self, nums, k):
        def check(mid):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= mid:
                    count += 1
                    i += 1
                i += 1
            return count >= k

        l,r = min(nums),max(nums)

        while l<r:
            mid = (l+r)//2

            if check(mid):
                r = mid
            else:
                l = mid + 1

        return l




        