class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        patterns = {}
        pattern_list = []

        best = max(str1, str2)

        for index in range(len( best )):
            pattern_list.append( best[0:index + 1] )

        for pattern in pattern_list:
            if len(str1.replace(pattern, "")) == 0 and len(str2.replace(pattern, "")) == 0:
                patterns[pattern] = 0
        
        print(patterns)
        good_pattern = ""

        for k, v in patterns.items():
            if len(k) > len(good_pattern) or good_pattern == "":
                good_pattern = k
        
        return good_pattern

        
