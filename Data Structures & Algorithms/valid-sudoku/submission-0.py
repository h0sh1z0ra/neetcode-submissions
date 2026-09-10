class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()  # (type, typeNo., val)

        for r in range(9):
            for c in range(9):
                # Existence checks
                if board[r][c] == ".":
                    continue
                
                if (("r", r, board[r][c]) in seen or
                    ("c", c, board[r][c]) in seen or
                    ("s", (r//3, c//3), board[r][c]) in seen):

                    return False
                
                seen.add(("r", r, board[r][c]))
                seen.add(("c", c, board[r][c]))
                seen.add(("s", (r//3, c//3), board[r][c]))
        
        return True
                