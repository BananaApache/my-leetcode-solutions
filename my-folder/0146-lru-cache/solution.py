
class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {} # (int) key -> (Node) node
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def prepend(self, node):
        prevNode = self.head
        nextNode = self.head.next

        prevNode.next = node
        nextNode.prev = node

        node.next = nextNode
        node.prev = prevNode

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
            self.prepend(node)
            return node.val
        else:
            return -1
            
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            # update it
            newNode = self.hashmap[key]
            newNode.val = value
            self.remove(newNode)
        else:
            # add it
            newNode = Node(key, value)
            self.hashmap[key] = newNode

        self.prepend(newNode)

        if len(self.hashmap) > self.capacity:
            lastNode = self.tail.prev
            self.remove(lastNode)
            del self.hashmap[lastNode.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
