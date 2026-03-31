class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # edge case
        if len(s1) > len(s2):
            return False # s1 should always be smaller or equal to s2

        # s1 = "ab"
        # s2 = "eidbaooo"
        #       12    

        # s1Map = {a: 1, b: 1}
        # s2MovingMap = {e: 1, i: 1}

        # decrement count of left from map, if 0 remove
        # increment left
        # increment right
        # add right to map

        s1Map = {}
        s2Map = {}

        for char1, char2 in zip(s1, s2):
            s1Map[char1] = s1Map.get(char1, 0) + 1
            s2Map[char2] = s2Map.get(char2, 0) + 1

        left = 0
        right = len(s1) - 1
        while right < len(s2):
            if s1Map == s2Map:
                return True

            if s2Map[s2[left]] == 1:
                del s2Map[s2[left]]
            else:
                s2Map[s2[left]] -= 1
            left += 1

            right += 1
            if right < len(s2):
                s2Map[s2[right]] = s2Map.get(s2[right], 0) + 1

        return False

