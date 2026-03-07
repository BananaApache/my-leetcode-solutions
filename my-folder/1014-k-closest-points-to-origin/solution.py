class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # import heapq

        # distToCoord = {}

        # for point in points:
        #     x, y = point
        #     dist = x**2 + y**2

        #     distToCoord[dist] = distToCoord.get(dist, []) + [[x, y]]

        # # make minHeap
        # minHeap = list(distToCoord.keys())
        # heapq.heapify(minHeap)

        # result = []

        # # stop when k is 0
        # while k > 0:
            
        #     # get min
        #     minDist = heapq.heappop(minHeap)

        #     # stop when k is 0 OR Coord list is empty
        #     while k > 0 and distToCoord[minDist]:
        #         result.append(distToCoord[minDist].pop())
        #         k -= 1

        # return result

        minHeap = []

        for x, y in points:
            minHeap.append([x**2 + y**2, x, y])

        heapq.heapify(minHeap)

        result = []

        while k > 0:
            _, x, y = heapq.heappop(minHeap)
            result.append([x, y])
            k -= 1
        
        return result

