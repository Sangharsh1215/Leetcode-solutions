# Last updated: 8/18/2025, 11:52:14 PM
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        maxi = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            maxi = max(right-left + 1, maxi)
        return maxi

        