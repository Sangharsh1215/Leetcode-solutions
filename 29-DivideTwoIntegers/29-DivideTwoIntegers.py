class Solution(object):
    def divide(self, n, m):
        if n == -2**31 and m == -1:  
            return 2**31 - 1
        if n == m:
            return 1
        if n == -m:
            return -1
        negative = (n < 0) ^ (m < 0)
        n, m = abs(n), abs(m)
        q = 0
        while n >= m:
            tempm, mult = m,1
            while n >= (tempm << 1):
                tempm <<= 1
                mult <<= 1
            n -= tempm
            q += mult
        return max(-2**31, min(2**31 - 1, -q if negative else q))