class Solution:
    def romanToInt(self, s: str) -> int:
        
        symbol2value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        nums = []
        for char in s:
            nums.append(symbol2value[char])

        # edge case where nums is length 1
        if len(nums) < 2:
            return nums[0]

        result = 0
        for index in range(0, len(nums) - 1):
            num = nums[index]
            nextNum = nums[index + 1]

            if num < nextNum:
                result -= num
            else:
                result += num

        result += nums[-1]

        return result

