class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {} # (int index, boolean buying) -> int profit

        def dfs(index, buying):
            # base cases
            if index >= len(prices):
                return 0
            if (index, buying) in dp:
                return dp[(index, buying)]

            # BUYING
            if buying:
                price = -prices[index] + dfs(index + 1, not buying)
                dp[(index, buying)] = price
            # SELLING
            else:
                price = prices[index] + dfs(index + 2, not buying)
                dp[(index, buying)] = price
            # COOLDOWN
            cooldown = dfs(index + 1, buying)

            newPrice = max(price, cooldown)
            dp[(index, buying)] = newPrice
            return newPrice

        print(dp)

        return dfs(0, True)

