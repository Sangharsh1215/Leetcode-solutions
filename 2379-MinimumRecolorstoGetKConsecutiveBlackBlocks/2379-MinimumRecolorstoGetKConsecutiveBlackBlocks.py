class Solution(object):
    def minimumRecolors(self, blocks, k):
        n = len(blocks)

        miniop = currW = blocks[:k].count('W')

        for i in range(k,len(blocks)):
            if blocks[i-k] == 'W':
                currW -= 1
            if blocks[i] == 'W':
                currW += 1
            miniop = min(currW,miniop)

        if miniop == 0:
            return 0
        return miniop 


        