# Last updated: 4/5/2025, 2:01:10 AM
class Solution(object):
    def sumSubarrayMins(self, arr):
        mod = 10**9 + 7
        def NSE(arr):
            n = len(arr)
            nse = [0]*n
            st = []

            for i in range(n-1,-1,-1):
                while st and arr[st[-1]] >= arr[i]:
                    st.pop()
                nse[i] = n if not st else st[-1]
                st.append(i)

            return nse

        def PSEE(arr):
            n = len(arr)
            psee = [0]*n
            st = []
            for i in range(n):
                while st and arr[st[-1]] > arr[i]:
                    st.pop()
                psee[i] = -1 if not st else st[-1]
                st.append(i)

            return psee


        n = len(arr)
        nse = NSE(arr)
        psee = PSEE(arr)
        total = 0

        for i in range(n):
            left = i - psee[i]
            right = nse[i] - i

            total = (total +(left*right*arr[i])) % mod

        return total



        
        