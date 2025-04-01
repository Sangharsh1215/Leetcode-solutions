# Last updated: 4/1/2025, 4:48:29 PM
class Solution(object):
    def mostPoints(self, questions):
        n = len(questions)
        dp = [-1]* n


        def check(questions,i,dp):

            if i >= n:
                return 0
            
            if dp[i] != -1:
                return dp[i]

            solve = questions[i][0] + check(questions,i+questions[i][1]+1,dp)
            skip =  check(questions,i+1,dp)

            dp[i] = max(solve,skip)

            return dp[i]

        return check(questions,0,dp)

        