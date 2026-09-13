class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pasTri = [[1] * (i+1) for i in range(rowIndex+1)]

        for row in range(2, rowIndex+1):
            for num in range(1, row):
                pasTri[row][num] = pasTri[row-1][num-1] + pasTri[row-1][num]
        
        return pasTri[-1]