class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        entire_product = 1
        has_zero = False

        for index in range(len(nums)):
            if has_zero and nums[index] == 0:
                entire_product = 0 
                break

            elif nums[index] == 0:
                has_zero = True
                continue

            entire_product = nums[index] * entire_product

        res = []

        for index in range(len(nums)):
            if has_zero:
                if nums[index] == 0:
                    res.append(entire_product)
                else:
                    res.append(0)
            else:
                res.append(int(entire_product / nums[index]))

        return res

