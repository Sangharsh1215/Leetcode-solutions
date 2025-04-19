# Last updated: 4/20/2025, 1:58:01 AM
class Solution(object):
    def countAndSay(self, n):
        def next_sequence(s):
            result = []
            i = 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                    count += 1
                result.append(str(count) + s[i])
                i += 1
            return ''.join(result)
        
        result = "1"
        for _ in range(n - 1):
            result = next_sequence(result)
        return result

            