class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        result = []

        for num in nums:
            if not result:
                result.append(num)
            else:
                result.append(num + result[-1])
            
        return result
        
