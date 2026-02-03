class Solution:
    def isHappy(self, n: int) -> bool:
        
        # edge cases
        if n == 1 or n == 100:
            return True

        # initialization
        seen = set()

        # convert to list
        digits = list(str(n))

        # stop when sumSquares already seen or sumSquares is 1
        while (n not in seen) and (n != 1):
            # store result in seen
            seen.add(n)

            # reset sumSquares
            n = 0

            # get sum of squares of digits
            for digit in digits:
                n += int(digit)**2
            
            # update new digits
            digits = list(str(n))
            
        
        return n == 1

