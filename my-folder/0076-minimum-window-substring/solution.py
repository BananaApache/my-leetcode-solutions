class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # minimum of result has to be length of t OR 0
        # brute force is to generate all substrings of s containing all letters of t and get smallest
        # sliding window
        # keep moving right until found all characters in t
        # then try to move left to remove any unnecessary characters
        # then reset left at the next right

        # s = "AAAB"
        # t = "AAB"

        # instance: A->0, B->1
        # curr window: AAA

        # edge case
        if len(s) < len(t):
            return ""

        result = ""
        resultLength = float('inf')
        
        freqT = defaultdict(int)
        for char in t:
            freqT[char] += 1

        left = 0
        currFreq = defaultdict(int)
        have = 0
        need = len(freqT)
        for right in range(len(s)):
            # found a char from t
            if s[right] in freqT:
                currFreq[s[right]] += 1
                if currFreq[s[right]] == freqT[s[right]]:
                    have += 1

            # found all chars from t
            while have == need:
                if right - left + 1 < resultLength:
                    result = s[left : right + 1]
                    resultLength = right - left + 1
                # try to move left while its current frequency bigger or equal to 1
                if s[left] in freqT:
                    if currFreq[s[left]] == freqT[s[left]]:
                        have -= 1
                    currFreq[s[left]] -= 1
                left += 1

        return result

