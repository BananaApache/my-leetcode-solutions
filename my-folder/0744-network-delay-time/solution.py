class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # SOUNDS LIKE DJIKSTRA

        # maximum of shortest weighted path from k to all n nodes

        adjMap = defaultdict(list)
        for a, b, time in times:
            adjMap[a].append( (time, b) )

        minHeap = [(0, k)]
        heapq.heapify(minHeap)
        visited = set()
        result = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visited:
                continue

            visited.add(node)
            result = max(result, time)
            
            for newTime, neighbor in adjMap[node]:
                if neighbor not in visited: 
                    heapq.heappush( minHeap, (newTime + time, neighbor) )

        if len(visited) == n:
            return result
        else:
            return -1

