class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify_max(nums)

        while k > 0: # stop when k is 0
            kth = heapq.heappop_max(nums)
            k -= 1

        return kth

