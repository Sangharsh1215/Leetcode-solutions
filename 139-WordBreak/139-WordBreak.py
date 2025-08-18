# Last updated: 8/19/2025, 1:23:48 AM
class Solution(object):
    def wordBreak(self, s, wordDict):
        wordset = set(wordDict)
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True

        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordset:
                    dp[i] = True
                    break
        return dp[n]

        