# Last updated: 4/12/2025, 12:13:57 AM
class Solution(object):
    def countSymmetricIntegers(self, low, high): 
        l = 0

        for i in range(low,high+1):
            s = str(i)
            k = len(s)
            if k % 2 == 0:
                mid = k//2
                left = sum(int(ch) for ch in s[:mid])
                right = sum(int(ch) for ch in s[mid:])
                if left == right:
                    l += 1

        return l


        