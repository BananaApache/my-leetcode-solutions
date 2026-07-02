class Solution:
    def countSubstrings(self, s: str) -> int:

        result = 0

        for index in range(len(s)):
            # odd
            l, r = index, index
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1

            # even
            l, r = index, index + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
        
        return result
        
        # def isP(left, right):
        #     while left < right:
        #         if s[left] != s[right]:
        #             return False
        #         left += 1
        #         right -= 1
            
        #     return True

        # result = 0
        # seen = set()

        # def dfs(left, right):
        #     nonlocal result
        #     # base case
        #     if (left, right) not in seen and isP(left, right):
        #         seen.add( (left, right) )
        #         result += 1
        #     if right >= len(s) - 1:
        #         return

        #     dfs(left + 1, right + 1)
        #     dfs(left, right + 1)
        
        # dfs(0, 0)

        # return result


