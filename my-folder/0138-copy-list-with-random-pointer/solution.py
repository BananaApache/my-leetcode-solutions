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
        
        originalToNew = {None: None}

        newHead = head
        dummy = Node(0)
        node = dummy

        while newHead:
            newNode = Node(newHead.val)
            node.next = newNode
            originalToNew[newHead] = newNode
            node = node.next
            newHead = newHead.next

        curr = head
        while curr:
            if curr.random:
                originalToNew[curr].random = originalToNew[curr.random]
            
            curr = curr.next

        return originalToNew[head]
        
