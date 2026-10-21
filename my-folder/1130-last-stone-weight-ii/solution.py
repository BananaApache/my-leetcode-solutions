class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        
        # dp[index] = [ [- -] [+ -] [- +] [+ +] ]
        # dp[index] represents all combinations of stones[index : ]

        dp = [ set() for _ in range(len(stones)) ]
        dp[-1] = {-stones[-1], stones[-1]}
        for index in range(len(dp) - 2, -1, -1):
            for factor in [ -1,1,-1,1 ]:
                for second in dp[index + 1]:
                    dp[index].add(factor * stones[index] + second)

        smallest = 101
        for num in dp[0]:
            if num >= 0:
                smallest = min(num, smallest)
        return smallest

