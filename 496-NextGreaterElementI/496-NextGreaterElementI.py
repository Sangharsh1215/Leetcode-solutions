# Last updated: 4/1/2025, 10:58:03 PM
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        l = []

        for num in nums1:
            i = nums2.index(num)

            while i < m-1:
                if nums2[i+1] > num:
                    l.append(nums2[i+1])
                    break
                else:
                    i += 1

            if i == m-1:
                l.append(-1)

        return l


        