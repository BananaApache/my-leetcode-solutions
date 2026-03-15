class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # intervals = sorted(intervals, key=lambda x: x[0])
        # result = []
        # left = 0

        # # [[1,3],[2,6],[8,10],[15,18]]
        # #   1           2              

        # while left < len(intervals):
        #     right = left
        #     maxEnd = intervals[left][1]
        #     while right < len(intervals) and (intervals[left][0] <= intervals[right][0] and intervals[right][0] <= maxEnd):
        #         maxEnd = max(maxEnd, intervals[right][1])
        #         right += 1

        #     result.append([intervals[left][0], maxEnd])
        #     left = right

        # return result

        intervals = sorted(intervals, key=lambda x: x[0])
        result = [intervals[0]]

        for start, end in intervals[1:]:
            last = result[-1]
            if last[0] <= start and start <= last[1]:
                result[-1][1] = max(last[1], end)
            else:
                result.append([start, end])

        return result

