class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # can use two pointer in even or odd cases

        result = ""
        for index in range(len(s)):
            # odd
            left = index
            right = index
            while (0<=left and right<len(s)) and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            if right - left + 1 >= len(result):
                result = s[left : right + 1]
            
            # even
            left = index
            right = index+1
            while (0<=left and right<len(s)) and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            if right - left + 1 >= len(result):
                result = s[left : right + 1]
        return result
