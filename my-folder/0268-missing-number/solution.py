class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        sortedNums = sorted(nums)

        for index in range(len(sortedNums)):
            if index != sortedNums[index]:
                return index
        
        return len(sortedNums)

