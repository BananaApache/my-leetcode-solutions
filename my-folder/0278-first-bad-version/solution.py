# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        #  L     M        R        
        # [1, 2, 3, 4, 5]
        #           B
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            print("checking", mid, "from", left, right)
            if not isBadVersion(mid): # search right
                left = mid + 1
            else: # search left
                if not isBadVersion(mid - 1):
                    return mid
                right = mid - 1

