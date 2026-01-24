class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        
        alphabet = "abcdefghijklmnopqrstuvzwxyz0123456789"
        
        alphanums = ""

        for letter in s:
            if letter in alphabet:
                alphanums += letter

        return alphanums == alphanums[::-1]
        
