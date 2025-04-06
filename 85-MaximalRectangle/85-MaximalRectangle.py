# Last updated: 4/6/2025, 11:08:40 PM
class Solution(object):
    def maximalRectangle(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        prefsum = [[0]* m for _ in range(n)]

        def largestRectangleArea(arr):
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



        for j in range(m):
            for i in range(n):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 0:
                    prefsum[i][j] = 0
                else:
                    prefsum[i][j] = prefsum[i-1][j] + 1 if i > 0 else 1


        maxarea = 0
        for i in range(n):
            maxarea = max(maxarea,largestRectangleArea(prefsum[i]))

        return maxarea


        
        