class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # if len(s) == 0:
        #     return 0
        
        # biggestSubstring = s[0]
        # substring = s[0]
        # maxLength = 1

        # for index1 in range(len(s)):
        #     for index2 in range(index1 + 1, len(s)):
        #         if s[index2] not in substring:
        #             substring += s[index2]
        #         else:
        #             if len(substring) > maxLength:
        #                 maxLength = len(substring)
        #                 biggestSubstring = substring
                    
        #             substring = s[index1 + 1]
        #             break
        
        # if len(substring) > maxLength:
        #     maxLength = len(substring)
        #     biggestSubstring = substring

        # return maxLength

        charSet = set()
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            result = max(result, r - l + 1)

        return result


