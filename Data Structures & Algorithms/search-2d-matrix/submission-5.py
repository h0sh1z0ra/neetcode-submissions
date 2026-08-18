class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        intervals = []
        for row in matrix:
            intervals.append((row[0], row[-1]))
        

        idx = 0
        for interval in intervals:
            if target >= interval[0] and target <= interval[-1]:
                return target in matrix[idx]
            idx += 1
            
        return False
