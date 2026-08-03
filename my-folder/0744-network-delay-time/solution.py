class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # take the max time

        adjMap = defaultdict(list) # (weight, node)
        for u, v, w in times:
            adjMap[u].append( (w, v) )

        result = 0
        minHeap = [ (0, k) ] # (weight, node)
        seen = set()
        heapq.heapify(minHeap)
        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in seen:
                continue
            seen.add(node)
            result = max(result, weight)

            for newWeight, neighbor in adjMap[node]:
                if neighbor not in seen:
                    heapq.heappush(minHeap, (weight + newWeight, neighbor) )


        if len(seen) == n:
            return result
        else:
            return -1

