# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # # edge cases
        # if head.next is None: # one node, n has to be 1, return empty
        #     return None
        
        # slow = head
        # fast = head
        # count = 0
        
        # # stop when fast is null or fast.next is null -> fast not null and fast.next not null
        # while fast is not None and fast.next is not None:
        #     slow = slow.next
        #     fast = fast.next.next

        #     count += 1

        # if fast is None:
        #     length = count*2 + 1
        # else:
        #     length = count*2 + 2

        # position = length - n - 1
        # print(position)

        # # position - 1 = 2
        # # count = 2
        # # 1,2,3,4,5
        # #     1

        # if position == 0:
        #     return head.next

        # count = 0
        # node = head
        # while count < position - 1:
        #     node = node.next
        #     count += 1

        # print(node.val)
        
        # if node.next and node.next.next is None:
        #     node.next = None
        # else:
        #     node.next = node.next.next

        # return head

        if head.next is None: # one node, n has to be 1, return empty
            return None

        dummy = ListNode(0, next=head)

        left = dummy
        right = head
        count = n
        while count > 0 and right:
            right = right.next
            count -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next
        

