class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        long_word, short_word = (str1, str2) if len(str1) > len(str2) else (str2, str1)

        choices = []

        for index in range(len(short_word)):
            choices.append(short_word[:index + 1])

        choices.reverse()

        for choice in choices:
            if ''.join(long_word.split(choice)) == '' and ''.join(short_word.split(choice)) == '':
                return choice

        return ""
