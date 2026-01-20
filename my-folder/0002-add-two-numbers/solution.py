# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        node = newList
        carryover = 0

        while l1 != None or l2 != None or carryover:
            if l1 != None:
                v1 = l1.val
            else:
                v1 = 0
            if l2 != None:
                v2 = l2.val
            else:
                v2 = 0

            sum = v1 + v2 + carryover

            if sum >= 10:
                carryover = 1
                sum = sum - 10
            else:
                carryover = 0

            node.next = ListNode(sum)

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

            node = node.next
        
        return newList.next
