class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []

        # items mapped to count
        itemToCount = {}
        for num in nums:
            itemToCount[num] = 1 + itemToCount.get(num, 0)

        # count mapped to array of item(s)
        countToItems = {}
        for item, count in itemToCount.items():
            countToItems[count] = countToItems.get(count, []) + [item]

        for index in range(len(nums), -1, -1):
            if countToItems.get(index, None):
                # stop when either the Items is empty OR k <= 0
                # complement: len(Items) > 0 and k > 0
                while len(countToItems[index]) > 0 and k > 0:
                    result.append(countToItems[index].pop())
                    k -= 1

        return result

            
