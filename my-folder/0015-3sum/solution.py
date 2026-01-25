class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # [-1, 0, 1]
        # [-4, -1, -1, 0, 1, 2]

        # create a set to keep track of seen nums
        prev = None
        # initialize result array
        result = []
        # sort array too
        nums = sorted(nums)

        # start looping through nums
        for index in range(0, len(nums) - 2):
            # add that num to set if not there already, if there skip
            if nums[index] == prev:
                continue
            else:
                prev = nums[index]

            # take left and right index
            leftPointer = index + 1
            rightPointer = len(nums) - 1

            # while left < right
            while leftPointer < rightPointer:
                # add them
                total = nums[leftPointer] + nums[rightPointer]
                # if sum bigger than 0 - nums[index] -> decrease Right Pointer
                if total > 0 - nums[index]:
                    rightPointer -= 1
                # if sum smaller than 0 - nums[index] -> increase Left Pointer
                elif total < 0 - nums[index]:
                    leftPointer += 1
                # if sum equal, then add to result array
                else:
                    result.append([nums[index], nums[leftPointer], nums[rightPointer]])
                    # pick random one pointer to move
                    leftPointer += 1
                    while nums[leftPointer] == nums[leftPointer - 1] and leftPointer < rightPointer:
                        leftPointer += 1
        
        # return result array
        return result

