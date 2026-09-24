class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        valids = "abcdefghijklmnopqrstuvwxyz0123456789"
        valids = set(valids)

        newS = ""
        for char in s:
            if char.lower() in valids:
                newS += char.lower()

        left = 0
        right = len(newS) - 1

        while left <= right:
            # while left < len(s) and s[left].lower() not in valids:
            #     left += 1
            # while right >= 0 and s[right].lower() not in valids:
            #     right -= 1
            
            if newS[left] != newS[right]:
                return False
            left += 1
            right -= 1

        return True

