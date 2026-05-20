class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        
        result = []

        def dfs(permutation, index):
            # base case
            if index == len(nums):
                result.append(permutation)
                return
            
            dfs(permutation + [nums[index]], index + 1)

            curr = nums[index]
            while not (index >= len(nums) or curr != nums[index]):
                index += 1
            dfs(permutation, index)
        
        dfs([], 0)
        return result

