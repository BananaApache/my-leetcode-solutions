class Solution:
    def longestPalindrome(self, s: str) -> str:

        result = s[0]
        for index in range(len(s)):
            left = index
            right = index + 1
            while 0<=left and right<len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            if (right - left + 1) > len(result):
                result = s[left : right + 1]

            left = index
            right = index
            while 0<=left and right<len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            if (right - left + 1) > len(result):
                result = s[left : right + 1]

        return result

