class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:


        #~ SECOND TRY
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        def generateList(word):
            output = []
            for index in range(len(word)):
                for letter in alphabet:
                    if letter != word[index]:
                        output.append( word[ : index] + letter + word[index + 1 : ] )
            return output

        wordList = set(wordList)
        q = deque([ (beginWord, 1) ])
        while q:
            word, path = q.popleft()
            print(word)
            if word == endWord:
                return path

            for newWord in generateList(word):
                if newWord in wordList:
                    q.append( (newWord, path+1) )
                    wordList.remove(newWord)
        
        return 0

        #~ FIRST TRY        
        # bfs shortest path from beginWord to endWord
        # construct adjMap with word -> [neighbors that are one letter away]
        # graph will be undirected
        # node will be a word
        # graph construction will be O(n squared * 10)

        # def oneAway(word1, word2):
        #     count = 0
        #     for index in range(len(word1)):
        #         if word1[index] != word2[index]:
        #             count += 1
        #             if count > 1:
        #                 return False
        #     return True

        # allWord = wordList + [beginWord]
        # adjMap = defaultdict(set)
        # for index in range(len(allWord)):
        #     for word2 in allWord[index + 1 : ]:
        #         word1 = allWord[index]
        #         if oneAway(word1, word2):
        #             adjMap[word1].add(word2)
        #             adjMap[word2].add(word1)
        
        # print(adjMap)
        
        # # bfs
        # q = deque([(beginWord, 1)])
        # seen = set([beginWord])
        # while q:
        #     word, path = q.popleft()
        #     if word == endWord:
        #         return path

        #     for neighbor in adjMap[word]:
        #         if neighbor not in seen:
        #             q.append( (neighbor, path+1) )
        #             seen.add(neighbor)

        # return 0

