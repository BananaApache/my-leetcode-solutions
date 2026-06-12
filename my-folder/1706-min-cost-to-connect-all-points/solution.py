class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # for every point
        # find closest

        def getDistance(points1, points2):
            return abs(points1[0] - points2[0]) + abs(points1[1] - points2[1])

        minHeap = [ (0, points[0]) ] # ( distance, [x, y] )
        heapq.heapify(minHeap)
        visited = set()
        totalDistance = 0

        while minHeap:
            if len(visited) == len(points):
                break
            distance, points1 = heapq.heappop(minHeap)
            if (points1[0], points1[1]) in visited:
                continue
            totalDistance += distance
            visited.add( (points1[0], points1[1]) )

            for points2 in points:
                if (points2[0], points2[1]) not in visited:
                    newDistance = getDistance(points1, points2)
                    heapq.heappush(minHeap, (newDistance, points2) )

        return totalDistance

