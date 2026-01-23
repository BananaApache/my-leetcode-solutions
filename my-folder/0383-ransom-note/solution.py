class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(ransomNote) > len(magazine):
            return False

        magazine = list(magazine)
        
        for letter in ransomNote:

            if letter not in magazine:
                return False # not there so invalid ransom note
            
            magazine[magazine.index(letter)] = '#'

        return True

