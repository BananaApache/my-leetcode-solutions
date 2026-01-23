class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # 'abcddee'
        # 'aabc'
        # 'abacba'
        # 'bbbbba'
        # 'aabb'
        # 'aaab'
        # 'loveleetcode'

        freq = {}

        for letter in s:
            freq[letter] = 1 + freq.get(letter, 0)
        
        for index in range(len(s)):
            if freq[s[index]] == 1:
                return index
        
        return -1



