class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        # initialize longestSub
        longestSub = ""

        # get shortest string of the two
        shortestString = min(str1, str2)
        longestString = max(str1, str2)

        # get all possible substrings that are multiples of longer one
        possibles = []
        for index in range(0, len(shortestString)):
            if len(longestString) % (index + 1) == 0:
                possibles.append(shortestString[0 : index + 1])

        # loop through all possibles
        for possible in possibles:
            # if Shorter == possible * (len(Shorter) / len(possible))
            if shortestString == possible * int(len(shortestString) / len(possible)) and longestString == possible * int(len(longestString) / len(possible)):
                longestSub = possible
            #    AND 
            #    Longer == possible * (len(Longer) / len(possible)) -> set longestSub to possible

        # return longestSub
        return longestSub

