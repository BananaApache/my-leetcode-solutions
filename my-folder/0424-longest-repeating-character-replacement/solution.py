class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # edge cases:
        if len(s) == 1:
            return 1

        # initialize
        freq = {}

        # 0 1 2 3 4 5
        # A B A B B A
        #   L       R   

        maxLength = 0
        left = 0
        maxFreq = 0
        # loop through string with right pointer
        for right in range(len(s)):
            # add char at right pointer to freq
            freq[s[right]] = freq.get(s[right], 0) + 1
            maxFreq = max(maxFreq, freq[s[right]])

            # while window not valid
            while (right - left + 1) - maxFreq > k:
                # decrease count of char at left
                freq[s[left]] = freq[s[left]] - 1
                # keep incrementing left pointer until valid
                left += 1

            # each time it is still valid adjust max
            maxLength = max(maxLength, right - left + 1)

        return maxLength

