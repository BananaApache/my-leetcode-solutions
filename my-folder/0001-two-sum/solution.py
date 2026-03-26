class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #  0 1  2 3
        # [2,11,6,7], target = 9
        #                   
        # 7->0,-2->1,3->2

        hashmap = {}

        for index in range(len(nums)):
            num = nums[index]
            if num not in hashmap:
                hashmap[target - num] = index
            else:
                return [index, hashmap[num]]

