class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        output = ""

        for index in range(max(len(word1), len(word2))):
            if index >= len(word1):
                output += word2[index]
            elif index >= len(word2):
                output += word1[index]
            else:
                output += word1[index]
                output += word2[index]

        return output
