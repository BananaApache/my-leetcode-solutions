class Solution:
    def removePalindromeSub(self, s: str) -> int:
        
        # check first entire string is palindrome
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                break
            left += 1
            right -= 1
        if left >= right:
            return 1
        else:
            return 2

