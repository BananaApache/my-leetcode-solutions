class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        # BOTTOM UP
        # dp[index]: is max of points from questions[index : end]
        dp = [0] * len(questions)
        dp[-1] = questions[-1][0]

        for index in range(len(dp) - 2, -1, -1):
            
            if index + questions[index][1] + 1 < len(dp):
                dp[index] = max(questions[index][0] + dp[index + questions[index][1] + 1], 0 + dp[index + 1])
            else:
                dp[index] = max(questions[index][0], 0 + dp[index + 1])
        
        return dp[0]

        # TOP DOWN (took 16 minutes)
        # state: which question we are at now = index
        # dfs(index): means max points from questions[index : end]
        # recurrence: get max of (take and skip) + current points of the question we are at
        # cache[index]: is max points from questions[index : end]

        # cache = {}

        # def dfs(index):
        #     # base case
        #     if index >= len(questions):
        #         return 0
        #     if index in cache:
        #         return cache[index]
            
        #     # current points
        #     currPoints = questions[index][0]

        #     #                 take current                                   skip current
        #     totalPoints = max(currPoints + dfs(index + questions[index][1] + 1), 0 + dfs(index + 1) )
        #     cache[index] = totalPoints
        #     return totalPoints
        
        # return dfs(0)

