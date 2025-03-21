// Last updated: 3/21/2025, 4:26:09 PM
class Solution(object):
    def removeDuplicates(self, nums):
        seen = set()
        index = 0

        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[index] = num
                index += 1
        return index

        