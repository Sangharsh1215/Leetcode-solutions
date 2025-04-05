# Last updated: 4/6/2025, 12:22:41 AM
class Solution(object):
    def removeKdigits(self, num, k):
        n = len(num)
        st = []
        if k == n:
            return '0'

        for i in range(n):
            while st and k > 0 and st[-1] > num[i]:
                st.pop()
                k -= 1
            st.append(num[i])

        while st and k > 0:
            st.pop()
            k -= 1

        if not st:
            return '0'
        res = ''
        while st:
            res += st[-1]
            st.pop()

        res = res[::-1]
        res = res.lstrip('0')

        return res if res else '0'

            