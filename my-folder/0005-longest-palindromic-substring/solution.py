class Solution:
    def longestPalindrome(self, s: str) -> str:

        result = ""
        
        for index in range(len(s)):
            # odd 
            l, r = index, index
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(result):
                    result = s[l : r + 1]
                l -= 1
                r += 1
            
            l, r = index, index + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(result):
                    result = s[l : r + 1]
                l -= 1
                r += 1

        return result

