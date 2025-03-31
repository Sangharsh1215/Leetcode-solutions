# Last updated: 3/31/2025, 4:07:21 PM
class Solution(object):
    def putMarbles(self, weights, k):
        if k == 1:
            return 0

        split = []

        for i in range(len(weights)-1):
            split.append(weights[i]+weights[i+1])
        i = k-1

        split.sort()

        max_score = sum(split[-i:])
        min_score = sum(split[:i])

        res = max_score - min_score 
        return res

        

        