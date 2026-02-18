"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
        
        hashmap = { None: None }

        # first pass
        node = head
        while node:
            hashmap[node] = Node(node.val)
            node = node.next

        # second pass
        node = head
        while node:
            copy = hashmap[node]
            copy.next = hashmap[node.next]
            copy.random = hashmap[node.random]
            node = node.next

        return hashmap[head]


