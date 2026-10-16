class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        
        # work backwards

        wordSet = set(wordDict)
        lengths = set()
        for word in wordSet:
            lengths.add(len(word))

        # dp[index]: whether or not s[index : ] can be made from wordDict
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for index in range(len(s) - 1, -1, -1):
            for length in lengths:
                if index + length <= len(s) and s[index : index + length] in wordSet:
                    dp[index] = dp[index] or dp[index + length]
        return dp[0]
        
