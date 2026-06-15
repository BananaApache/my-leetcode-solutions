class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        maxHeap = nums
        heapq.heapify_max(nums)

        while k:
            result = heapq.heappop_max(nums)
            k -= 1

        return result



