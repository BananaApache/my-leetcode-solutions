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

        # first make array of pointers to all nodes in order
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next

        #  0 1 2 3
        # [1,2,3,4]
        #    2 1   
        #  1->4->2->3->None      

        # [1]
        #  3
        #  

        #  0 1
        # [1,2]
        #    3    
        #  1->2->none     

        #  0 1 2 3 4
        # [1,2,3,4,5]
        #      3     
        #  1->5->2->4->3     

        left = 0
        right = len(nodes) - 1
        while left < right:
            # set L next to R
            nodes[left].next = nodes[right]
            # increment left
            left += 1
            if left < right:
                nodes[right].next = nodes[left]
            else:
                nodes[right].next = None
            # decrement right
            right -= 1

        if left == right:
            nodes[right].next = None

        head = nodes[0]

