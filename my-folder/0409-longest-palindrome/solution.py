class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        freq = list(freq.values())

        result = 0
        hasOdd = False

        for f in freq:
            if f % 2 == 0:
                result += f
            else:
                result += f - 1
                hasOdd = True

        return result + 1 if hasOdd else result

