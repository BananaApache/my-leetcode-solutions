class Solution:
    def partition(self, s: str) -> list[list[str]]:
        
        # try each prefix word
        # if prefix word is Palindrome, run dfs
        # once reached end, add to result

        def isPalindrome(left, right):
            # 01234
            # aabaa

            # 0123
            # abba

            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        result = []

        curr = []
        def dfs(index):
            # base case
            if index == len(s):
                result.append(curr.copy())
                return

            for right in range(index + 1, len(s) + 1):
                newWord = s[index : right]
                if isPalindrome(index, right - 1):
                    curr.append(newWord)
                    dfs(right)
                    curr.pop()
        
        dfs(0)
        return result


