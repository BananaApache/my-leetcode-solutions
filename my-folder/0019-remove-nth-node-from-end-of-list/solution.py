# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        hashmap = {}
        index = 0
        node = head
        while node:
            hashmap[index] = node
            node = node.next
            index += 1
        
        length = len(hashmap)
        prev = length - n - 1
        goal = length - n

        if prev >= 0:
            hashmap[prev].next = hashmap[goal].next
            return head
        else:
            return head.next
