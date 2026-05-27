
class TrieNode:

    def __init__(self, node=None, isEnd=False):
        self.node = node
        self.isEnd = isEnd
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        index = 0
        while index < len(word):
            if word[index] not in node.children:
                newNode = TrieNode(word[index])
                node.children.update({word[index] : newNode})
                node = newNode
            else:
                node = node.children[word[index]]
            index += 1

        node.isEnd = True

    def search(self, word: str) -> bool:
        index = 0
        node = self.root
        while index < len(word):
            if word[index] not in node.children:
                return False
            
            node = node.children[word[index]]
            index += 1
        
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        index = 0
        node = self.root
        while index < len(prefix):
            if prefix[index] not in node.children:
                return False
            
            node = node.children[prefix[index]]
            index += 1
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
