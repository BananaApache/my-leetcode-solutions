class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        time = 0
        waiting = deque()

        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        maxHeap = list(freq.values())
        heapq.heapify_max(maxHeap)

        while maxHeap or waiting: # stop when BOTH maxHeap empty AND waiting empty
            # check waiting and try to add to maxHeap
            if waiting:
                first = waiting[0] # <tuple> (tasks left, time that can be added back)

                if first[1] == time: # if its time, add back and remove from waiting
                    waiting.popleft()
                    heapq.heappush_max(maxHeap, first[0])

            if maxHeap:
                tasksLeft = heapq.heappop_max(maxHeap)
                
                if tasksLeft > 1:
                    waiting.append( (tasksLeft - 1, time + n + 1) )

            time += 1
                
                
        return time

