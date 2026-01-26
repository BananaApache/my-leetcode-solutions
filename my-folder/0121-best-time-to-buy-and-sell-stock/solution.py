class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # [7,1,5,3,6,4] length 6
        #  0 1 2 3 4 5

        # edge cases
        # length of prices is 1
        if len(prices) == 1:
            return 0

        maxDifference = 0
        # set left pointer to 0
        left = 0
        # loop through entire array with right pointer but from 1..len(prices)
        for right in range(1, len(prices)):
            # check maxDifference
            maxDifference = max(prices[right] - prices[left], maxDifference)
            
            # but if R - L < 0
            if prices[right] - prices[left] < 0:
                # set L = R
                left = right

        return maxDifference

