class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # [1,2,3,4] even. len = 4
        # [1,2]

        # [1,2,3,4,5] odd. len = 5
        # [1,2]

        length = len(s)

        for index in range(0, (length // 2)):
            swap_position = length - 1 - index

            tmp = ''

            tmp = s[index]
            s[index] = s[swap_position]
            s[swap_position] = tmp


        
        
