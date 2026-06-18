class Solution:
    def numDecodings(self, s: str) -> int:

        if s == "0":
            return 0

        dp = [0] * len(s)
        
        if s[-1] != 0:
            dp[-1] = 1

        dp.append(1)
        dp.append(0)

        for index in range(len(s) - 1, -1, -1):
            if int(s[index]) == 0:
                dp[index] = 0
            elif int(s[index : index + 2]) > 26:
                dp[index] = dp[index + 1]
            else:
                dp[index] = dp[index + 1] + dp[index + 2]
        
        return dp[0]


        # OLD TRIED SOLUTION
        
        # hashmap = {}

        # def dfs(startIndex, endIndex):
        #     # base case
        #     if endIndex > len(s):
        #         return 0
        #     elif endIndex == len(s):
        #         hashmap[ (startIndex, endIndex) ] = 1
        #         return 1

        #     if int(s[startIndex + 1 : endIndex + 1]) > 26:
        #         return 0

        #     if (endIndex + 1, endIndex + 1) in hashmap:
        #         leftDecodings = hashmap[ (endIndex + 1, endIndex + 1) ]
        #     else:
        #         leftDecodings = dfs(endIndex + 1, endIndex + 1)
        #         hashmap[ (endIndex + 1, endIndex + 1) ] = leftDecodings
        #     if (endIndex + 1, endIndex + 2) in hashmap:
        #         rightDecodings = hashmap[ (endIndex + 1, endIndex + 2) ]
        #     else:
        #         rightDecodings = dfs(endIndex + 1, endIndex + 2)
        #         hashmap[ (endIndex + 1, endIndex + 2) ] = rightDecodings


        #     return leftDecodings + rightDecodings
        
        # return dfs(0, 0) + dfs(0, 1)

