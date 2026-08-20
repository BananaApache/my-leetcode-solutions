class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # keep track of previous needed leftover in hashmap for O(1) lookup

        # nums = [2,11,15,7]
        #         0 1  2  3
        # hashmap = 2: 0, 11: 1           
        # target = 9

        hashmap = {}
        for index in range(len(nums)):
            difference = target - nums[index]
            if difference in hashmap:
                return [hashmap[difference], index]
            else:
                hashmap[nums[index]] = index
