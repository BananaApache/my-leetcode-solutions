class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) < 2:
            return len(s)
        
        left = 0
        result = 0
        substring = set()

        for right in range(len(s)):
            while s[right] in substring:
                substring.discard(s[left])
                left += 1

            substring.add(s[right])
            result = max(result, len(substring))

        return result

