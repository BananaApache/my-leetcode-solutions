class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        dp = [False] * len(s)
        dp.append(True)

        for index in range(len(dp) - 2, -1, -1):
            for word in wordDict:
                if s[index : ].startswith(word):
                    dp[index] = dp[index + len(word)]
                if dp[index]:
                    break
        
        return dp[0]

        # BACKTRACKING DFS APPROACH, NO CACHE
        # # base cases:
        # # - doesnt start with word
        # # - length of word node longer than s

        # maxLength = len(s)

        # def dfs(word):
        #     # base cases
        #     if not s.startswith(word):
        #         return False
        #     elif len(word) == maxLength:
        #         return word == s
            
        #     for subword in wordDict:
        #         newWord = word + subword
        #         if len(newWord) <= maxLength and dfs(newWord):
        #             return True

        #     return False

        # return dfs("")

