class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        output = []

        for index in range(len(word1) + len(word2)):
            try:
                output.append(word1[index])
            except:
                pass
            
            try:
                output.append(word2[index])
            except:
                pass
        
        return "".join(output)
        
