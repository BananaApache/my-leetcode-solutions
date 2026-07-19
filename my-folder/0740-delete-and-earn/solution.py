class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        freqMap = defaultdict(int)
        for num in nums:
            freqMap[num] += 1
        
        values = sorted(list(freqMap.keys()))
        dp = [0] * len(values) # dp[index] = max points from values[index] onwards
        dp[-1] = values[-1] * freqMap[values[-1]]

        for index in range(len(dp) - 2, -1, -1):
            points = freqMap[values[index]] * values[index]
            
            # take it and take next dp that is not values[index] + 1
            if index + 1 < len(values):
                if values[index] + 1 == values[index + 1]:
                    if index + 2 < len(values):
                        points += dp[index + 2]
                else:            
                    points += dp[index + 1]
            
            skip = dp[index + 1] if index + 1 < len(values) else 0

            dp[index] = max(points, skip)

        return dp[0]

