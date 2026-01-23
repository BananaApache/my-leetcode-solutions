class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        evens = []
        odds = []

        for index in range(len(nums)):
            if nums[index] % 2 == 0:
                evens.append(nums[index])
            else:
                odds.append(nums[index])

        return evens + odds

