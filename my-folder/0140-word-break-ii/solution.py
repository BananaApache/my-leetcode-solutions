class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        
        # s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
        # 0 1 2 3 4 5 6 7 8 9 
        # c a t s a n d d o g
        # c a t 
        # try topdown backtracking with dfs                    
        # dfs(index, curr): traverse s starting at index and test all words in wordDict with current string
        wordSet = set(wordDict)
        lengths = set()
        for word in wordSet:
            lengths.add(len(word))

        result = []
        curr = []
        def dfs(index):
            # base case
            if index == len(s):
                result.append(" ".join(curr))
                return
            
            for length in lengths:
                if index + length <= len(s) and s[index : index + length] in wordSet:
                    curr.append(s[index : index + length])
                    dfs(index + length)
                    curr.pop()
        dfs(0)
        return result

