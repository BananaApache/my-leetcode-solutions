
class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                newNode = TrieNode()
                node.children.update({char : newNode})
                node = newNode
            else:
                node = node.children[char]
        
        node.isEnd = True

    def search(self, word: str) -> bool:
        
        def dfs(node, index):
            # base case
            if index == len(word):
                return (node.isEnd)
            
            if word[index] != ".":
                if word[index] not in node.children:
                    return False
                else:
                    return dfs(node.children[word[index]], index + 1)
            
            else:
                for trieNode in node.children.values():
                    if dfs(trieNode, index + 1):
                        return True
                    
                return False

        node = self.root

        return dfs(node, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
