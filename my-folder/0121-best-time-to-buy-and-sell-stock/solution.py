class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        result = 0
        left = 0
        
        for right in range(len(prices)):
            result = max(result, prices[right] - prices[left])

            if prices[right] < prices[left]:
                left = right
        
        return result

