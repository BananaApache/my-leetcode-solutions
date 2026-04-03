class Solution:
    def equalFrequency(self, word: str) -> bool:

        # abcc

        # freq
        # a 1
        # b 1
        # c 2

        # counts
        # 1 2
        # 2 1

        # keys = 1,2

        
        freq = {}
        for char in word:
            freq[char] = freq.get(char, 0) + 1
        
        counts = list(freq.values())
        countMap = {}
        for count in counts:
            countMap[count] = countMap.get(count, 0) + 1

        print(freq)
        print(countMap)

        keys = list(countMap.keys())

        if len(keys) == 1 and (keys[0] == 1 or countMap[keys[0]] == 1):
            return True

        if len(keys) != 2:
            return False
        
        if (countMap[keys[0]] == 1 and countMap[keys[1]] == 1) and ((keys[0] == 1 or keys[1] == 1) or (max(keys) == min(keys) + 1)):
            return True
        
        if (max(keys) == min(keys) + 1) and (countMap[max(keys)] == 1):
            return True

        if (1 in countMap and countMap[1] == 1):
            return True

        return False

