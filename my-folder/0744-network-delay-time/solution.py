class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # need adjacency map
        # looks like djikstra shortest weighted path
        # but need to reach all nodes, so take max of shortest weighted paths of all from k
        # add to seen only when popping because could find shorter path during minHeap

        adjMap = defaultdict(list) # (weight, node)
        for source, target, weight in times:
            adjMap[source].append( (weight, target) )
        
        result = 0
        minHeap = [ (0,k) ]
        heapq.heapify(minHeap)
        seen = set()

        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in seen:
                continue
            seen.add(node)
            result = max(result, weight)

            for newWeight, newNode in adjMap[node]:
                heapq.heappush(minHeap, (weight + newWeight, newNode) )
        
        if len(seen) == n:
            return result
        else:
            return -1

