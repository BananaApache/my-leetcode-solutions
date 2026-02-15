class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:

        from collections import Counter

        m = nums
        c = Counter(m)
        freq = Counter(c.values())

        for x in m:
            f = c[x]
            if freq[f] == 1:
                return x

        return -1
        
