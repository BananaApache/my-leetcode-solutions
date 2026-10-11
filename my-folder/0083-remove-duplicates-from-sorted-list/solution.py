# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        
        # seen = {1}
        # p   n    
        # 1 - 1

        prev = None
        node = head
        seen = set()
        while node:
            if node.val in seen:
                nextNode = node.next
                prev.next = nextNode
                node = nextNode
            else:
                seen.add(node.val)
                prev = node
                node = node.next
        return head

