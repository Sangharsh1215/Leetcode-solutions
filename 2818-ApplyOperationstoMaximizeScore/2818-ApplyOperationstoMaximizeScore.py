# Last updated: 3/29/2025, 4:18:55 PM
class Solution(object):
    def maximumScore(self, nums, k):
        N = len(nums)
        MOD = 10**9 + 7
        res = 1

        prime_scores = []
        for n in nums:
            score = 0
            for f in range(2,int(sqrt(n) + 1)):
                if n % f == 0:
                    score += 1
                while n%f == 0:
                    n = n//f
            if n >= 2:
                score += 1
            prime_scores.append(score)

        left = [-1]* N
        right = [N] * N

        stack = []
        for i,s in enumerate(prime_scores):
            while stack and prime_scores[stack[-1]] < s:
                index = stack.pop()
                right[index] = i
            if stack:
                left[i] = stack[-1]
            stack.append(i)


        min_heap = [(-n,i) for i, n in enumerate(nums)]
        heapify(min_heap)

        while k>0:
            n,index = heappop(min_heap)
            n = -n
            score = prime_scores[index]
            
            left_cnt = index - left[index]
            right_cnt = right[index] - index

            count = left_cnt * right_cnt
            operations = min(count,k)
            res = (res*pow(n,operations,MOD))% MOD
            k -= operations

        return res
        