class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # state: index
        # decisions: choose from lengths in wordDict
        # dfs(index): can s[index : -1] be broken down into words from wordDict
        # recurrence: If there exists a valid word starting here and the rest of the string can also be segmented, then this state is True.

        wordDict = set(wordDict)
        lengths = set()
        cache = {}

        for word in wordDict:
            lengths.add(len(word))
        
        def dfs(index):
            # base case
            if index == len(s):
                return True # yes can be broken down because it is empty
            if index in cache:
                return cache[index]
            
            # canBreak = False

            for length in lengths:
                # before i jump, have to check that current substring is in wordDict
                if (index + length) <= len(s) and s[index : index + length] in wordDict:
                    if dfs(index + length):
                        cache[index] = True
                        return True

            cache[index] = False
            return False
        
        return dfs(0)

