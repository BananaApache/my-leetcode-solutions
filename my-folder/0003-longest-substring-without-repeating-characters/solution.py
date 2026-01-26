class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # edge cases:
        # length 0 or 1
        if len(s) == 0 or len(s) == 1:
            return len(s)

        # charSet = ab
        # a b c d c c   length 6
        # L R        
        #                

        # initializing
        charSet = set()
        left = 0
        maxLength = 1

        # add char at Left to charSet
        charSet.add(s[left])

        # keep moving Right index from 1..len(s)
        for right in range(1, len(s)):
            # but if char at Right in charSet -> we found a duplicate
            if s[right] in charSet:
                # remove char at Left from charSet
                charSet.remove(s[left])
                # increment Left
                left += 1
                # while the char at previous Left not equal to char at Right AND Left < Right
                while s[left - 1] != s[right] and left < right:
                    # remove char at Left from charSet
                    charSet.remove(s[left])
                    # increment Left
                    left += 1

                # add char at Right to charSet
                charSet.add(s[right])
            # else
            else:
                # add char at Right to charSet
                charSet.add(s[right])
                # set new maxLength
                maxLength = max(maxLength, len(charSet))

        return maxLength

