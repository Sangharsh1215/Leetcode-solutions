# Last updated: 4/5/2025, 10:58:37 PM
class Solution(object):
    def asteroidCollision(self, a):
        st = []
        for i in range(len(a)):
            if a[i] > 0:
                st.append(a[i])
            else:
                while st and (abs(a[i]) > st[-1]) and st[-1] > 0:
                    st.pop()
                if st and (st[-1] == abs(a[i])):
                    st.pop()
                elif not st or (st[-1] < 0):
                    st.append(a[i])
        return st


        