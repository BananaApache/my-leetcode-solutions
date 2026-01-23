class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        
        firstElement = colors[0]
        secondElement = colors[1]

        colors.append(firstElement)
        colors.append(secondElement)

        count = 0

        for index in range(0, len(colors) - 2):
            left = colors[index]
            middle = colors[index + 1]
            right = colors[index + 2]

            if left == right and left != middle:
                count += 1
        
        return count

