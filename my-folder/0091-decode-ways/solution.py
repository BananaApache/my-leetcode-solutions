class Solution:
    def numDecodings(self, s: str) -> int:
        
        # BOTTOM UP APPROACH
        # state: index
        # dfs(index): num decodings possible from index to end of s
        # dp[index]: num decodings possible from index to end of s
        # set dp[index] to (dp[index + 1] if s[index] valid) + (dp[index + 2] if s[index : index + 2] valid)

        dp = [0] * len(s)
        dp.append(1)

        for index in range(len(s) - 1, -1, -1):
            if s[index] == '0':
                continue
            
            dp[index] = dp[index + 1]

            if index + 2 <= len(s) and int(s[index : index + 2]) in range(10, 27):
                dp[index] += dp[index + 2]
            
        return dp[0]

        # TOP DOWN APPROACH
        # state: index
        # dfs(index): num decodings possible from index to end of s
        # recurrence: try the index then [index:index + 1]. after do dfs(new index) of the ones that were valid
        
        # cache = {}

        # def dfs(index):
        #     # base case
        #     if index == len(s):
        #         return 1
        #     if index in cache:
        #         return cache[index]
            
        #     if s[index] == '0':
        #         cache[index] = 0
        #         return 0
            
        #     decodings = dfs(index + 1)

        #     if index + 2 <= len(s) and int(s[index : index + 2]) in range(10, 27):
        #         decodings += dfs(index + 2)

        #     cache[index] = decodings
        #     return decodings
        
        # return dfs(0)

