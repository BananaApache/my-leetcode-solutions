class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for index in range(len(nums)):
            if freq.get(nums[index]):
                freq[nums[index]] += 1
            else:
                freq[nums[index]] = 1
        
        sorted_data = dict(sorted(freq.items(), key=lambda item: item[1]))

        data = list(sorted_data.keys())

        data.reverse()

        return data[:k]

