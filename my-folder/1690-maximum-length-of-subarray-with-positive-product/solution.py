class Solution:
    def getMaxLen(self, nums: list[int]) -> int:

        positive = negative = result = 0

        for num in nums:
            if num == 0:
                positive = negative = 0
            elif num > 0:
                positive += 1
                negative = negative + 1 if negative else 0
            else:
                positive, negative = (
                    negative + 1 if negative else 0,
                    positive + 1
                )

            result = max(result, positive)

        return result

