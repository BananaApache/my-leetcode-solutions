class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # use minHeap to always get closest of a point
        # add to seen only when we pop because pushing doesnt mean its shortest yet
        
        def getDistance(x1, y1, x2, y2):
            return abs( x2 - x1 ) + abs( y2 - y1 )

        seen = set()
        minHeap = [ (0, (points[0][0], points[0][1]) ) ]
        heapq.heapify(minHeap)
        output = 0

        while minHeap:
            if len(seen) == len(points):
                return output
            distance, currPoints = heapq.heappop(minHeap)
            x, y = currPoints

            if (x, y) in seen:
                continue

            output += distance
            seen.add( (x, y) )

            
            for x2, y2 in points:
                if (x2, y2) not in seen:
                    heapq.heappush(minHeap, (getDistance(x, y, x2, y2), (x2, y2)) )
        
        return output

