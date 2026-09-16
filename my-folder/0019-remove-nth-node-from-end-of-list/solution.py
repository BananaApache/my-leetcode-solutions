# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        
        # node = head
        # length = 0
        # while node:
        #     node = node.next
        #     length += 1
        # goal = length - n + 1

        # # get prev node
        # index = 1
        # node = head
        # prev = None
        # while index != goal:
        #     prev = node
        #     node = node.next
        #     index += 1
        
        # if prev:
        #     prev.next = node.next
        #     return head
        # else:
        #     return head.next
        
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

