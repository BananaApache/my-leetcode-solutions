
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(factorial(m + n - 2) / (factorial(m - 1) * factorial(n - 1)))
        

