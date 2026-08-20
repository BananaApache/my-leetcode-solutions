class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()
        if not s:
            return 0
        multiplier = 1
        if s[0] == "-":
            multiplier = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        
        result = 0
        for char in s:
            if not char.isdigit():
                break
            
            if char == "0" and not result:
                result = 0
                continue
            
            if char.isdigit():
                result = result * 10 + int(char)
        
        if not result:
            return 0
        print(result)
        result = int(result) * multiplier
        if result <= -2**31:
            return -2**31
        elif result >= 2**31 - 1:
            return 2**31 - 1
        else:
            return result

