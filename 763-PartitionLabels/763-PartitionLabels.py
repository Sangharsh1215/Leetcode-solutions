# Last updated: 3/30/2025, 5:50:32 PM
class Solution(object):
    def partitionLabels(self, s):
        n = len(s)
        mp = {}
        end = 0
        size = 0
        l = []

        for i,c in enumerate(s):
            mp[c] = i

        for i, st in enumerate(s):
            end = max(end,mp[st])
            
            size += 1
            if i == end:
                l.append(size)
                size = 0


        return l


        

        