class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        word = s[-1]
        index = len(s) - 1
        while word == "":
            index -= 1
            word = s[index]

        return len(word)

