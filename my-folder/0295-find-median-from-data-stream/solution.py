class MedianFinder:

    # LEFT heap and RIGHT heap
    # LEFT  = maxHeap
    # RIGHT = minHeap
    # ALWAYS TRUE: size(LEFT) <= size(RIGHT) + 1
    # ALWAYS TRUE: every element in LEFT <= every element in RIGHT
    #           -> maxHeap[0] <= minHeap[0]
    #           -> if not, pop from LEFT and move it to RIGHT

    def __init__(self):
        self.left = []
        self.right = []
        heapq.heapify_max(self.left)
        heapq.heapify(self.right)

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.left, num)
        if (self.right and self.left[0] > self.right[0]):
            popped = heapq.heappop_max(self.left)
            heapq.heappush(self.right, popped)
        
        if len(self.left) > len(self.right) + 1: # right is smaller
            # move biggest from left to right
            popped = heapq.heappop_max(self.left)
            heapq.heappush(self.right, popped)
        if len(self.right) > len(self.left) + 1: # left is smaller
            # move smallest from right to left
            popped = heapq.heappop(self.right)
            heapq.heappush_max(self.left, popped)

    def findMedian(self) -> float:
        totalLength = len(self.left) + len(self.right)
        if totalLength % 2 != 0:        
            if len(self.left) > len(self.right):
                return  self.left[0]
            if len(self.left) < len(self.right):
                return  self.right[0]
        else:
            # EVEN CASE
            return (self.left[0] + self.right[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
