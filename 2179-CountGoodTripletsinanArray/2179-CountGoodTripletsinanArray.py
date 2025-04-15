# Last updated: 4/16/2025, 12:46:20 AM
from bisect import bisect_left, insort
class Solution(object):
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)
        pos2 = [0] * n
        for i, v in enumerate(nums2):
            pos2[v] = i

        nums1_mapped = [pos2[v] for v in nums1]
        left = []
        left_count = [0] * n
        for i in range(n):
            idx = bisect_left(left, nums1_mapped[i])
            left_count[i] = idx
            insort(left, nums1_mapped[i])

        right = []
        right_count = [0] * n
        for i in range(n - 1, -1, -1):
            idx = bisect_left(right, nums1_mapped[i])
            right_count[i] = len(right) - idx
            insort(right, nums1_mapped[i])

        total = 0
        for i in range(n):
            total += left_count[i] * right_count[i]
        return total

            