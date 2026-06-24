class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cost.append(0)

        for index in range(len(cost) - 3, -1, -1):
            cost[index] = min(cost[index] + cost[index + 1], cost[index] + cost[index + 2])
        
        return min(cost[0], cost[1])

