class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        # state: index so far
        # dfs(index): returns minimum cost to travel days from days[index : end]
        # recurrence: choose minimum from trying [1,7,30] passes and add to current cost (try cache too)
        # cache[index]: returns minimum cost to travel days from days[index : end]

        cache = {}
        dayPass = [1, 7, 30]

        def dfs(index):
            # base case
            if index >= len(days):
                return 0
            if index in cache:
                return cache[index]
            
            newCost = float('inf')
            for dayIndex in range(len(dayPass)):
                newIndex = index
                while newIndex < len(days) and days[newIndex] < (days[index] + dayPass[dayIndex]): # stop when days[index] >= days[index] + dayPassLength
                    newIndex += 1
                
                newCost = min( newCost, costs[dayIndex] + dfs(newIndex) )
            
            cache[index] = newCost
            return newCost

        return dfs(0)

