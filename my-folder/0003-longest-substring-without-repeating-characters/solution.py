class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # sliding window technique
        # move window when met duplicate
        # keep track of biggest

        # 0 1 2 3 4 5 6 7
        # a b c a b c b b
        #     L   R        
        # seen = b,c

        if len(s) < 2:
            return len(s)

        result = 0
        left = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.discard(s[left])
                left += 1
            seen.add(s[right])
            result = max(result, len(seen))
        return result

