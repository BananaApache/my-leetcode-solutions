class Solution:
    def numDecodings(self, s: str) -> int:
        
        # state: index -> total decodings from index to end
        # cache: index -> total decodings

        cache = {}

        def dfs(index):
            # base case
            if index >= len(s):
                return 1 # got to end successfully

            if s[index] == '0':
                return 0
            if index in cache:
                return cache[index]
            
            decodings = dfs(index + 1)

            if index + 1 < len(s) and int(s[index : index + 2]) in range(10, 27):
                decodings += dfs(index + 2)
            
            cache[index] = decodings
            return decodings

        return dfs(0)

