class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        first = s[0:int(len(s)/2)].lower()
        second = s[int(len(s)/2):].lower()
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        print(vowels)
        firstCount = 0
        secondCount = 0
        for index in range(len(first)):
            if first[index] in vowels:
                firstCount += 1
            if second[index] in vowels:
                secondCount += 1
        return firstCount == secondCount
