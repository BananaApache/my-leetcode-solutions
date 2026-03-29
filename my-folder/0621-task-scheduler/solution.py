class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # always be taking task with highest frequency

        freqMap = defaultdict(int)
        for task in tasks:
            freqMap[task] += 1
        
        maxHeap = list(freqMap.values())
        heapq.heapify_max(maxHeap)

        q = deque()
        time = 0

        while q or maxHeap:
            time += 1

            if len(maxHeap) > 0:
                taskCount = heapq.heappop_max(maxHeap)
                if taskCount - 1 != 0:
                    q.append( (taskCount - 1, time + n) )

            if q and q[0][1] == time:
                taskCount, _ = q.popleft()
                heapq.heappush_max(maxHeap, taskCount)

        return time

