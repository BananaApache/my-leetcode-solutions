class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # get the total products to the left

        preProducts = [1]
        for index in range(1, len(nums)):
            preProducts.append( preProducts[index - 1] * nums[index - 1] )

        print(preProducts)
        
        # get the total products to the right
            # by reversing initial array

        postProducts = [1]
        reversedNums = nums[::-1]
        for index in range(1, len(reversedNums)):
            postProducts.append( postProducts[index - 1] * reversedNums[index - 1] )

        postProducts = postProducts[::-1]

        # loop through indexes and multiply item at index left times right
        result = []
        for index in range(len(nums)):
            result.append(preProducts[index] * postProducts[index])

        return result


