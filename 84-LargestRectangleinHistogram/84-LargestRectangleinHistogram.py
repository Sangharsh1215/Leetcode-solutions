# Last updated: 4/6/2025, 1:07:10 AM
class Solution(object):
    def largestRectangleArea(self, arr):
        n = len(arr)
        def NSE(arr):
            nse = [0]*n
            st = []
            for i in range(n-1,-1,-1):
                while st and arr[st[-1]] >= arr[i]:
                    st.pop()
                nse[i] = n if not st else st[-1]
                st.append(i)

            return nse

        def PSE(arr):
            psee = [0]*n
            st = []
            for i in range(n):
                while st and arr[st[-1]] > arr[i]:
                    st.pop()

                psee[i] = -1 if not st else st[-1]
                st.append(i)

            return psee

        nse = NSE(arr)
        pse = PSE(arr)

        maxi = 0

        for i in range(n):

            res = (nse[i] - pse[i] - 1)*arr[i]
            maxi = max(maxi,res)

        return maxi

        