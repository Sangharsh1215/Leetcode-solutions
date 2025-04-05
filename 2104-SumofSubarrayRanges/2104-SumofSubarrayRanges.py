# Last updated: 4/5/2025, 11:49:53 PM
class Solution(object):
    def subArrayRanges(self, arr):
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

        def PSEE(arr):
            psee = [0]*n
            st = []
            for i in range(n):
                while st and arr[st[-1]] > arr[i]:
                    st.pop()

                psee[i] = -1 if not st else st[-1]
                st.append(i)

            return psee

        def NGE(arr):
            st = []
            nge = [0]*n
            for i in range(n-1,-1,-1):
                while st and arr[st[-1]] <= arr[i]:
                    st.pop()
                nge[i] = n if not st else st[-1]
                st.append(i)
            return nge

        def PGE(arr):
            st = []
            pge = [0]*n
            for i in range(n):
                while st and arr[st[-1]] < arr[i]:
                    st.pop()
                pge[i] = -1 if not st else st[-1]
                st.append(i)
            return pge

        total = 0
        nse = NSE(arr)
        psee = PSEE(arr)
        nge = NGE(arr)
        pge = PGE(arr)
        for i in range(n):
            left1 = i - pge[i]
            right1 = nge[i] - i

            total += (left1*right1*arr[i])

            left2 = i - psee[i]
            right2 = nse[i] - i

            total -= (left2*right2*arr[i])   


        return total