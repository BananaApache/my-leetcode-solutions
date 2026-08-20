class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        freqMap = defaultdict(int)
        for letter in magazine:
            freqMap[letter] += 1
        
        for letter in ransomNote:
            if freqMap[letter] == 0:
                return False
            else:
                freqMap[letter] -= 1
        return True

