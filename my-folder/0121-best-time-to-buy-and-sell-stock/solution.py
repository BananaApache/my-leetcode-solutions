class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # [7,1,5,3,6,4]
        #    1       2 

        left = 0
        result = 0

        for right in range(len(prices)):
            profit = prices[right] - prices[left]
            if profit >= 0:
                result = max(result, profit)
            else:
                left = right

        return result

