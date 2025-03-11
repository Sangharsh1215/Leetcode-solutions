class Solution(object):
    def numberOfSubstrings(self, s):
        char = {'a':0, 'b':0, 'c':0}
        n = len(s)
        count = 0
        left = 0
        for right in range(n):
            char[s[right]] += 1

            while all(char[c]>0 for c in 'abc'):
                count += len(s) - right
                char[s[left]] -= 1
                left += 1
        return count
        