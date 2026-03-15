"""
(len(tasks) - 1) * 3 + len(tasks) = ONLY MINIMUM WHEN ALL THE SAME

["A","A","A"] n = 3
A i i i A i i i A
9

["A","B","A","B"] n = 3
A: 2, B: 2
A i i i B i i i A i i i B
13
OR
A B i i A B
6

["A","B","A"] n = 3
B A i i i A
A B i i A
!!! start with the item with most frequency then move to second most frequent and so on

["A","C","A","B","D","B"] n = 1
A: 2, B: 2, C: 1, D: 1

!!! always looking for next biggest frequency -> heap
!!! you idle when every letter is waiting -> set lookup

"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import deque
        freqDict = {}
        for task in tasks:
            freqDict[task] = freqDict.get(task, 0) + 1

        maxHeap = list(freqDict.values())
        heapq.heapify_max(maxHeap)

        q = deque()
        time = 0

        while maxHeap or q: # stop when maxHeap empty AND q empty
            if maxHeap:
                freq = heapq.heappop_max(maxHeap)
                freq -= 1
                if freq != 0:
                    q.append([freq, time + n])

            if q and q[0][1] == time:
                heapq.heappush_max(maxHeap, q.popleft()[0])

            time += 1

        return time

