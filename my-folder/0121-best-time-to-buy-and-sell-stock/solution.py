class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # [7,1,5,3,6,4]
        #    1       2       
        # result 5       

        #     

        left = 0
        result = 0

        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                result = max(result, prices[right] - prices[left])

        return result

