# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        node = dummy
        carryover = 0

        # l1 node needs to exist or l2 node needs to exist
        while l1 or l2:
            total = 0
            if not l2: # l2 is none
                total = l1.val + carryover
                carryover = 0
                l1 = l1.next
            elif not l1: # l1 is none
                total = l2.val + carryover
                carryover = 0
                l2 = l2.next
            else: # l1 and l2 both exists
                total = l1.val + l2.val + carryover
                carryover = 0
                l1 = l1.next
                l2 = l2.next

            if total >= 10:
                total -= 10
                carryover = 1
            
            node.next = ListNode(total)
            node = node.next

        if carryover == 1:
            node.next = ListNode(1)

        return dummy.next
            
