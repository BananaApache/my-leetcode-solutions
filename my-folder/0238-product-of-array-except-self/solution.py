
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]

        output = []

        for i in range(len(nums) - 1):
            prev = left[i]
            left.append(prev * nums[i])

        count = 0
        for num in list(reversed(nums))[:-1]:
            after = right[count]
            right.append(after * num)
            count += 1
        right = list(reversed(right))

        for i in range(len(left)):
            output.append(left[i] * right[i])

        return output


            

        



