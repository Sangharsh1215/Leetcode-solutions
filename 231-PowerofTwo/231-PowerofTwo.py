// Last updated: 3/19/2025, 11:41:16 PM
class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        if n == 1:
            return True
        while n > 1:
            if n % 2 == 1:
                return False
            n//=2

        return True

        