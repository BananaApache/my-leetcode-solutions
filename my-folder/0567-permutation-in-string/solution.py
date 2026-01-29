
from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # edge case:
        if len(s1) > len(s2):
            return False

        # initializing
        s1Map = defaultdict(int)
        for letter in s1:
            s1Map[letter] += 1

        s2Map = defaultdict(int)
        for letter in s2[0 : len(s1) - 1]: # only from s2 of index 0 to index length of s1 - 1
            s2Map[letter] += 1

        left = 0
        right = len(s1) - 1

        # first loop through s2 substring one time to initialize while right < len(s2)
        while right < len(s2):
            s2Map[s2[right]] += 1
            # if 2 dicts are equal
            if s1Map == s2Map:
                # then we found a match, return True
                return True
            
            # if s2Map[char at left] is 1
            if s2Map[s2[left]] == 1:
                # remove s2Map[char at left]
                del s2Map[s2[left]]
            # else
            else:
                # decrement count of s2Map[char at left]
                s2Map[s2[left]] = s2Map[s2[left]] - 1
            # incremenet left
            left += 1

            # increment right
            right += 1
            # add char at right to s2Map

        # return False
        return False
