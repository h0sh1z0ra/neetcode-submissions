class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pasTri = [[1] * (i+1) for i in range(numRows)]

        for row in range(2, numRows):
            for pos in range(1, row):
                pasTri[row][pos] = pasTri[row-1][pos-1] + pasTri[row-1][pos]
        
        return pasTri