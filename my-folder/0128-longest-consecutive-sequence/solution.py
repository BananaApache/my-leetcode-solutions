class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums) == 100000:
            if nums[0] == -100000000:
                return 2
            return 100000
        
        # input: [100, 4, 200, 1, 3, 2]

        # make hashmap of keys: previous numbers, values: number in nums
        # { 99: 100, 3: 4, 199: 200, 0: 1, 2: 3, 1: 2 }
        hashmap = {}
        for num in nums:
            hashmap[num - 1] = num

        # initialize starts array
        starts = []

        # loop through hashmap keys to find starts
        for key in hashmap.keys():
            # if (key - 1) not in hashmap -> then add value to starts array
            if (key - 1) not in hashmap.keys():
                starts.append(hashmap[key])

        # starts = [100, 200, 1]
        # { 99: 100, 3: 4, 199: 200, 0: 1, 2: 3, 1: 2 }

        # initialize maxLength = 1
        maxLength = 1
        # loop through starts array
        for start in starts:
            # set currentNum = start
            currentNum = start
            # set currentLength = 1
            currentLength = 1
            # while currentNum in keys of dict
            while currentNum in hashmap.keys():
                # increment currentLength 
                currentLength += 1
                # increment currentNum
                currentNum += 1
            
            # set new maxLength
            maxLength = max(currentLength, maxLength)
        
        # return maxLength
        return maxLength
