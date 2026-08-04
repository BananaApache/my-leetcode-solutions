class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # LGA < LGB
        # START: JFK
        # len(output) has to equal (len(tickets) + 1)
        # all tickets form at least one valid itinerary
        # must use all the tickets only once

        # doesnt need shortest path, just any path, cycles are allowed
        # build AdjMap, sort each neighbor list
        # avoid infinite loop but travel through cycles -> remove an item from neighbor list once visited
        # needs to be dfs to explore the whole path one by one
        # use a queue to store, neighbors, do not loop through neighbors, just look at start, once visiting, popleft

        # dfs(city): traverses city by city by popping its first neighbor, and traversing it. returns false if not whole

        adjMap = defaultdict(list)
        for start, end in tickets:
            adjMap[start].append(end)
        for node in adjMap:
            heapq.heapify(adjMap[node])

        result = []

        def dfs(city):
            nonlocal result
            # base case
            if not adjMap[city]:
                result.append(city)
                return
            
            while adjMap[city]:
                dfs(heapq.heappop(adjMap[city]))
            result.append(city)
            return
        
        dfs("JFK")
        return result[::-1]

