class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for index in range(len(nums)): 
            print(index)

            difference = target - nums[index]

            if hashmap.get(nums[index]) != None: # difference exists in hashmap
                return [hashmap.get(nums[index]), index]
            else: # difference not in hashmap, so add it
                hashmap.update({difference : index})

        print(hashmap)
