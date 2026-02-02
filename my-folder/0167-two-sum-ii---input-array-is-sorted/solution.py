class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # edge cases
        if len(numbers) == 2:
            return [1, 2]
        
        # init left = 0, right = len(numbers)
        left = 0
        right = len(numbers) - 1

        # keep looping while left smaller than right
        while left < right:
            total = numbers[left] + numbers[right]
            # if sum bigger than target,    
            if total > target:
                # decrement right because overshot
                right -= 1
            # if sum less than target,
            elif total < target:
                # increment left because undershot
                left += 1
            # if sum equal,
            else:
                # return left + 1, right + 1
                return [left + 1, right + 1]

