class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # # O(m + n) TC. Use binary search
        # intervals = []
        # for row in matrix:
        #     intervals.append((row[0], row[-1]))

        # idx = 0
        # for interval in intervals:
        #     if target >= interval[0] and target <= interval[-1]:
        #         return target in matrix[idx]
        #     idx += 1
            
        # return False

        ### Binary search: Search for row, then inside row
        left, right = 0, len(matrix)

        while left < right:
            mid = left + (right-left)//2

            if target > matrix[mid][-1]:
                left = mid + 1
            
            elif target < matrix[mid][0]:
                right = mid
            
            else:
                l = 0; r = len(matrix[mid])

                while l < r:
                    m = l + (r-l)//2
                    if target == matrix[mid][m]:
                        return True
                    if target > matrix[mid][m]:
                        l = m+1
                    else:
                        r = m
                return False
        return False