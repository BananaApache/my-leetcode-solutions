class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}

        def dfs(index):
            if index == len(s):
                return 1

            if index in cache:
                return cache[index]

            if s[index] == '0':
                return 0

            # Decode one digit
            total = dfs(index + 1)

            # Decode two digits, if valid
            if index + 1 < len(s) and 10 <= int(s[index:index + 2]) <= 26:
                total += dfs(index + 2)

            cache[index] = total
            return total

        return dfs(0)
