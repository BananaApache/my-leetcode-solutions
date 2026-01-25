
from collections import deque

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # [1,1,1,2,2,3], k = 2

        # initialize a result array 
        result = []

        freq = {}

        for index in range(len(nums)):
            freq[nums[index]] = 1 + freq.get(nums[index], 0)
        
        # fill the frequency hashmap
        countMap = []

        # fill countMap from 1..len(nums)
        for index in range(len(nums)):
            countMap.append(deque())
        
        for item, count in freq.items():
            countMap[count - 1].append(item)

        # loop through the keys reversed
        for q in countMap[::-1]:
            # keep popping until q empty OR length of result is k
            while len(q) != 0 and len(result) != k:
                result.append(q.popleft())

        # return result array
        return result

