class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s:
            return True
        
        pointer1 = 0

        for pointer2 in range(len(t)):
            if s[pointer1] == t[pointer2]:
                if pointer1 == len(s) - 1:
                    return True
                else:
                    pointer1 += 1

        return False

