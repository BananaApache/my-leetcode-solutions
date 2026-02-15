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

        # store list of 3 tuple: (node1, node2, next)?

        nodes = []

        node = head
        while node:
            nodes.append(node)
            node = node.next

    
        
        for index in range(len(nodes) // 2):
            nextNode = head.next
            head.next = nodes[len(nodes) - index - 1]
            if head.next == nextNode:
                head.next.next = None
                return
            else:
                head.next.next = nextNode
                head = nextNode
        
        head.next = None
