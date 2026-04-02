class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        result = [[1]]

        for _ in range(0, numRows - 1):
            row = []
            topLength = len(result[-1])
            for index in range(0, topLength + 1):
                if index == 0:
                    row.append(result[-1][0])
                elif index == topLength:
                    row.append(result[-1][-1])
                else:
                    row.append(result[-1][index - 1] + result[-1][index])
            
            result.append(row)

        return result

