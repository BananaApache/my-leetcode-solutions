class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # length 9
        # 0 1 2 3 4 5 6 7 8
        # c a t s a n d o g
        # F F F F F F F F F
        # cats, dog, sand, and, cat
        # lenghts = 4,3

        wordDict = set(wordDict)
        lengths = set()
        for word in wordDict:
            lengths.add(len(word))
        # smallestLength = min(lengths)

        dp = [False] * len(s)
        dp.append(True)

        for index in range(len(s), -1, -1):
            for length in lengths:
                if index + length <= len(s):
                    subword = s[index : index + length]
                    if subword in wordDict and not dp[index]:
                        dp[index] = True and dp[index + length]
                        
        
        print(dp)
        return dp[0]

