class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        
        sMap = Counter(s)
        tMap = Counter(t)

        for key in tMap:
            if tMap[key] != sMap.get(key, -1):
                return key

