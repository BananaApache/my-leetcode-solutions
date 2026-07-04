class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        result = [ [intervals[0][0], intervals[0][1]] ]

        for start, end in intervals:
            prevStart, prevEnd = result[-1]
            if start >= prevStart and start <= prevEnd:
                result[-1][1] = max(end, prevEnd)
            else:
                result.append( [start, end] )

        return result

