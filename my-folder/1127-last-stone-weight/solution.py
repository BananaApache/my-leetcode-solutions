class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # build max heap
        maxHeap = stones
        heapq.heapify_max(maxHeap)

        # stop looping when maxHeap has one element
        while len(maxHeap) > 1:
            stone1 = heapq.heappop_max(maxHeap)
            stone2 = heapq.heappop_max(maxHeap)

            difference = stone1 - stone2

            if difference != 0:
                heapq.heappush_max(maxHeap, difference)

        return maxHeap[0] if maxHeap else 0


