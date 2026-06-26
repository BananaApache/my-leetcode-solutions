class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        #           (cost, day)
        days.append((0, 399))
        
        for index in range(len(days) - 2, -1, -1):
            
            minCost = costs[0] + days[index + 1][0]
            foundWeek = False
            foundMonth = False
            for nextIndex in range(index + 1, len(days)):
                # 7 day
                if not foundWeek and days[index] + 7 <= days[nextIndex][1]:
                    minCost = min(minCost, costs[1] + days[nextIndex][0])
                    foundWeek = True
                if days[index] + 30 <= days[nextIndex][1]:
                    minCost = min(minCost, costs[2] + days[nextIndex][0])
                    foundMonth = True
                    break
            
            days[index] = (minCost, days[index])

        print(days)

        return days[0][0]

