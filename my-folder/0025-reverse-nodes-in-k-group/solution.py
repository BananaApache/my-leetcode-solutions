# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        
        # to reverse in linear time and constant space
        # 1 -> 2 -> 3
        # initialize to prev to None
        # store node.next in tmp
        # set node.next to prev
        # set prev to node
        # move node to tmp (which was node.next)
        # stop when k hits 0

        # only need to reverse [len(LinkedList) // k] times
        node = head
        length = 0
        while node:
            node = node.next
            length += 1

        dummy = ListNode()
        times = length // k
        node = head
        tail = dummy
        while times > 0:
            reverseK = k
            first = node
            prev = None
            while reverseK > 0:
                nextNode = node.next
                node.next = prev
                prev = node
                node = nextNode
                reverseK -= 1
            
            if not dummy.next:
                dummy.next = prev
            tail.next = prev
            tail = first
            times -= 1
        tail.next = node
        
        return dummy.next


