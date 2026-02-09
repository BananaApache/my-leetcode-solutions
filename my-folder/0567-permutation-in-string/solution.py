class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # edge case
        if len(s2) < len(s1):
            return False

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        s1Freq = {}
        s2Freq = {}
        for letter in alphabet:
            s1Freq[letter] = 0
            s2Freq[letter] = 0

        for index in range(len(s1)):
            s1Freq[s1[index]] += 1
            s2Freq[s2[index]] += 1

        matches = 0
        for letter in s1Freq.keys():
            if s1Freq[letter] == s2Freq[letter]:
                matches += 1

        left = 0
        
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            s2Freq[s2[right]] += 1
            if s2Freq[s2[right]] == s1Freq[s2[right]]:
                matches += 1
            elif s2Freq[s2[right]] == s1Freq[s2[right]] + 1:
                matches -= 1

            s2Freq[s2[left]] -= 1
            if s2Freq[s2[left]] == s1Freq[s2[left]]:
                matches += 1
            elif s2Freq[s2[left]] == s1Freq[s2[left]] - 1:
                matches -= 1
            left += 1

        return matches == 26


