
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

def esteban_method(x):
    product = 1

    for i in range(1, x + 1):
        product = product * i

    return product

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # return int(factorial(m + n - 2) / (factorial(m - 1) * factorial(n - 1)))
        return int(esteban_method(m + n - 2) / (esteban_method(m - 1) * esteban_method(n - 1)))
        

