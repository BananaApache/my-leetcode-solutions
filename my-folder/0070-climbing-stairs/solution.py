class Solution:
    def climbStairs(self, n: int) -> int:

        # BOTTOMUP TABULAR

        # its just fibonacci
        # dp = [1] * (n + 1)

        # for index in range(2, len(dp)):
        #     dp[index] = dp[index - 1] + dp[index - 2]
        
        # return dp[n]

        prev = 1
        curr = 1
        while n > 1:
            curr, prev = prev + curr, curr
            n -= 1
        return curr

        # TOPDOWN APPROACH MEMOIZATION
        # thinking of decision tree with two paths at each node
        # take 1 step
        # take 2 step
        # base case is when you reach n
        # can try topdown with memoization
        # use step as key

        # cache = {}

        # def dfs(step):
        #     # base case
        #     if step in cache:
        #         return cache[step]
        #     if step > n:
        #         return 0
        #     if step == n:
        #         return 1

        #     left = dfs(step + 1)
        #     right = dfs(step + 2)

        #     cache[step] = left + right
        #     return left + right
        
        # return dfs(0)

