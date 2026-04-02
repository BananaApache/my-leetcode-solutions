class Solution:
    def isUgly(self, n: int) -> bool:
        import math

        if n == 1:
            return True
        
        def isPrime(n):
            for index in range(2, int(math.sqrt(abs(n))) + 1):
                if n % index == 0:
                    return False
            
            return True

        # num = 7

        num = n
        while not isPrime(num):
            if num % 2 == 0:
                num = num / 2
            elif num % 3 == 0:
                num = num / 3
            elif num % 5 == 0:
                num = num / 5
            else:
                return False

        if num != 2 and num != 3 and num != 5:
            return False
        else:
            return True

