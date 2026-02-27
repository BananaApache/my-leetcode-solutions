
class ListNode:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = {}
        self.capacity = capacity

    # removes node from linked list
    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    # appends node to end of linked list
    def append(self, node):
        prevNode = self.tail.prev
        nextNode = self.tail
        prevNode.next = nextNode.prev = node
        node.next = nextNode
        node.prev = prevNode

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # update that key listnode to the most recently used (top of linked list)
            node = self.hashmap[key]

            self.remove(node)
            self.append(node)

            # return that value 
            return self.hashmap[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        
        self.hashmap[key] = ListNode(key, value)
        self.append(self.hashmap[key])

        # check length of hashmap
        if len(self.hashmap.keys()) > self.capacity: # LRUCache is at max capacity
            # evict the head of linked list
            lru = self.head.next
            self.remove(lru)
            del self.hashmap[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
