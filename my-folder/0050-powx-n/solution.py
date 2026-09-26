class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def pow(x, absN):
            if absN == 0:
                return 1
            elif absN % 2 == 0:
                return pow(x * x, absN / 2)
            else:
                return x * pow(x * x, (absN - 1) / 2)
        
        result = pow(x, abs(n))
        return result if n >= 0 else 1/result
