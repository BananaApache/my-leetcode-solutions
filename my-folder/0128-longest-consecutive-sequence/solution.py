class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashmap = {} # num -> prev

        for num in nums:
            hashmap[num] = num + 1
        
        starts = set()

        for key in hashmap:
            if (key - 1) not in hashmap:
                starts.add(key)
        
        result = 0
        for start in starts:
            currLength = 1
            nextNum = hashmap[start]
            while nextNum in hashmap:
                currLength += 1
                nextNum = hashmap[nextNum]
            result = max(result, currLength)    

        return result

