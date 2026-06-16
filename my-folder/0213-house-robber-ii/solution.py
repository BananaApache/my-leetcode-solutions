class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # base cases
        if len(nums) < 4:
            return max(nums)

        def subrob(nums):
            rob1, rob2 = 0, 0

            #   
            # [rob1, rob2, n, n+1, n+2, ...]
            #   ^          ^       rob1 represents sub decisions so far of everything behind n except rob2
            #          ^           rob2 represents not robbing n and sub decisions before                            
            for n in nums:
                tmp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = tmp
            
            return rob2

        return max (subrob(nums[1:]), subrob(nums[0:-1]))

