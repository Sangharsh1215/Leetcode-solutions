# Last updated: 4/13/2025, 7:38:37 PM
class Solution(object):
    def countGoodNumbers(self, n):
        MOD = 10**9 + 7
        even = (n+1)//2
        odd = n//2

        return pow(5,even,MOD)*pow(4,odd,MOD) % MOD