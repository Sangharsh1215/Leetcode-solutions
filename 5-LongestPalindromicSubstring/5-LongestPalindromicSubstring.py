# Last updated: 8/19/2025, 12:47:01 AM
class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        res = ""
        resmax = 0
        for i in range(n):
            l,r = i,i
            while l >= 0 and r<n and s[r] == s[l]:
                if (r-l+1) > resmax:
                    res = s[l:r+1]
                    resmax = r - l + 1
                l -= 1
                r += 1
            l,r = i,i+1
            while l >= 0 and r<n and s[r] == s[l]:
                if (r-l+1) > resmax:
                    res = s[l:r+1]
                    resmax = r - l + 1
                l -= 1
                r += 1

        return res
              

        