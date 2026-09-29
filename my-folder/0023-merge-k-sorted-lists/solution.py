# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        
        # lists is list of head listNodes
        # lists can be empty
        # can use minHeap to keep track of all current heads
        # heap push when adding new head and then traverse that head
        # stop when all lists empty head
        # question doesnt say if i am supposed to modify existing linkNodes in lists or create new ones?

        dummy = ListNode()
        node = dummy
        uniqueCount = count()

        minHeap = []
        heapq.heapify(minHeap)
        for index in range(len(lists)):
            if lists[index]:
                heapq.heappush(minHeap, (lists[index].val, next(uniqueCount), lists[index]) )
        
        while minHeap:
            _,_, newNode = heapq.heappop(minHeap)
            tmp = newNode.next
            node.next = newNode
            if tmp:
                heapq.heappush(minHeap, (tmp.val, next(uniqueCount), tmp) )
            node = node.next
        
        return dummy.next
