class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
            
        if len(s) == 1:
            return 1

        leftPointer = 0
        currLength = 1
        maxLength = 1
        
        for rightPointer in range(1, len(s)):
            
            while s[rightPointer] in s[leftPointer : rightPointer]: 
                # checking if next letter in substring already
                leftPointer += 1
            
            currLength = rightPointer - leftPointer + 1

            if currLength > maxLength:
                maxLength = currLength

        return maxLength

