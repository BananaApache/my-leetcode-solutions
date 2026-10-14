class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        
        # choices are skip current OR take max of arr[index : index + k]
        # the most we want to skip is 1 to optimize on the subarrays
        # base case is when the remaining is length k
        # dfs(index) is maximum total from arr[index : ]
        # dfs(i) = max{ dfs(index + 1) , max(arr[index : index + k]) + dfs(index + k) }

        cache = {}
        def dfs(index):
            # base case
            if index in cache:
                return cache[index]
            if index == len(arr):
                return 0

            curr = 0
            currMax = 0
            for right in range(1, k + 1):
                if index + right <= len(arr):
                    currMax = max(currMax, arr[index + right - 1])
                    curr = max( curr, right * currMax + dfs(index + right) )
            cache[index] = curr
            return cache[index]

        return dfs(0)

