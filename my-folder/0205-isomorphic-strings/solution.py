class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # a -> e
        # d -> g

        # s = egg
        # t = add

        t2s = {}
        s2t = {}

        for index in range(len(t)):
            if t[index] not in t2s:
                t2s[t[index]] = s[index]
            else:
                if s[index] != t2s[t[index]]:
                    return False

            if s[index] not in s2t:
                s2t[s[index]] = t[index]
            else:
                if t[index] != s2t[s[index]]:
                    return False

        return True

