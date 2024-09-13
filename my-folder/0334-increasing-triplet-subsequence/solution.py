class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        minimum = float('inf')
        middle = float('inf')

        for num in nums:

            # print(num)

            if num <= minimum:
                minimum = num
            
            elif minimum < num and num < middle:
                middle = num
            
            elif num > middle:
                return True

        return False

