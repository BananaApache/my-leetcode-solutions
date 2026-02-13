# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # # edge cases
        # if not head:
        #     return False

        # foundDuplicate = False
        # node = head

        # # 3 2 0 -4
        # #   1     

        # # keep looping while node still exists and foundDuplicate is false
        # while node and not foundDuplicate:
        #     if not isinstance(node.val, tuple):
        #         node.val = (node.val, True)
        #     else:
        #         foundDuplicate = True
        #         break
            
        #     node = node.next

        # return foundDuplicate




        # better solution actuallly
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

