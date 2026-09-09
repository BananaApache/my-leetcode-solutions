# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        # reverse time
        prev = None
        while mid:
            nextNode = mid.next
            mid.next = prev
            prev = mid
            mid = nextNode
        
        node1 = head
        node2 = prev
        while node2:
            nextNode1 = node1.next
            nextNode2 = node2.next
            node1.next = node2
            node2.next = nextNode1
            node1 = nextNode1
            node2 = nextNode2


