class Solution:
    def reverseWords(self, s: str) -> str:
        sentence = []
        s = list(reversed(s.split(" ")))
        for word in s:
            if not word.isspace() and word != "":
                sentence.append(word)

        return " ".join(sentence)
        
