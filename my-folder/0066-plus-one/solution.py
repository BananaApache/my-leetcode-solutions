class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits = digits[::-1]

        digits[0] += 1

        carryover = 0
        for index in range(len(digits)):
            digits[index] += carryover
            num = digits[index]
            if num >= 10:
                carryover = 1
                digits[index] = 0
            else:
                carryover = 0

        if carryover > 0:
            digits.append(1)

        digits = digits[::-1]
        
        return digits
            
