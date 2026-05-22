class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(substrings):
            for substring in substrings:
                for index in range(len(substring) // 2):
                    if substring[index] != substring[len(substring) - index - 1]:
                        return False
            
            return True
        
        # substrings ALWAYS non-empty
        # two paths:
        #   - add char to current str
        #   - start new substring starting with char

        result = []

        def backtrack(substrings, index):
            # base case
            if index == len(s):
                if isPalindrome(substrings):
                    result.append(substrings)
                return
            
            backtrack(substrings + [s[index]], index + 1)

            substrings[-1] += s[index]
            backtrack(substrings, index + 1)
        
        backtrack([s[0]], 1)
        return result

