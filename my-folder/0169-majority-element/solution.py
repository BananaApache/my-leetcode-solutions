class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        freq = {}
        halfLength = (len(nums) / 2)

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > halfLength:
                return num

