class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        
        # work backwards

        wordSet = set(words)
        lengths = set()
        smallest = 10001
        for word in wordSet:
            length = len(word)
            smallest = min(smallest, length)
            if length <= smallest * 2 + 6:
                lengths.add(length)

        result = []
        # dp[index]: whether or not s[index : ] can be made from wordDict
        for s in words:
            if len(s) < smallest * 2:
                continue
            wordSet.remove(s)
            dp = [False] * (len(s) + 1)
            dp[-1] = True
            for index in range(len(s) - 1, -1, -1):
                for length in lengths:
                    if index + length <= len(s) and s[index : index + length] in wordSet:
                        dp[index] = dp[index] or dp[index + length]
            if dp[0]:
                result.append(s)
            wordSet.add(s)
        return result

