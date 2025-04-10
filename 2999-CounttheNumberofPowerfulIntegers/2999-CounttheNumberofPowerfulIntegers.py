# Last updated: 4/11/2025, 12:02:48 AM
class Solution(object):
    def numberOfPowerfulInt(self, start, finish, limit, s):
        def call(x,s,limit):
            if len(x) < len(s):
                return 0
            if len(x) == len(s):
                return 0 if x<s else 1

            count = 0
            plen = len(x) - len(s)
            sufx = x[plen:]

            for i in range(plen):
                if int(x[i]) > limit:
                    count = count + (limit + 1)**(plen - i)

                    return count
                count = count + int(x[i])*(limit + 1)**(plen - i - 1)

            if sufx >= s:
                count = count + 1
            return count

        return call(str(finish),s,limit) - call(str(start-1),s,limit) 
        