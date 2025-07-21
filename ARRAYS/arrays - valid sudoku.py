# Problem 1.8 : Valid Sudoku board
# Validate if a 9 × 9 Sudoku board is valid based on Sudoku rules (no repeated digits in any row, column or 3 × 3 box).


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Check rows, columns and 3 × 3 boxes separately for duplicates using sets. Use a fresh set for each.
# Time  : O(n²)
# Space : O(n²)
class Solution1:
    def isValidSudoku(self, board):
        # Checking all 9 rows
        for row in range(9):
            seen = set()
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue                # skipping empty cells
                if val in seen:
                    return False            # duplicate found in row
                seen.add(val)

        # Checking all 9 columns
        for col in range(9):
            seen = set()
            for row in range(9):
                val = board[row][col]
                if val == ".":
                    continue                # skipping empty cells
                if val in seen:
                    return False            # duplicate found in column
                seen.add(val)

        # Checking all 9 sub-boxes (3 x 3) : BOX-LEVEL (9 BOXES)
        for box in range(9):
            seen = set()
            # Computing TOP-LEFT cell coordinates of current 3 x 3 grid
            row_base = (box // 3) * 3       # Row group : 0/1/2, 3/4/5, 6/7/8 -> mapped to 0, 3, 6. [000333666]
            col_base = (box % 3) * 3        # Column group : 0/1/2, 3/4/5, 6/7/8 -> mapped to 0, 3, 6. [036036036]
            for i in range(3):              # CELL LEVEL inside each box
                for j in range(3):
                    r = row_base + i
                    c = col_base + j
                    val = board[r][c]
                    if val == ".":
                        continue            # skipping empty cells
                    if val in seen:
                        return False        # duplicate in 3 x 3 box
                    seen.add(val)

        return True                         # no duplicates found, board is valid
    

# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Hash Set (One Pass) 
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use hash sets to track values in rows, columns and boxes during a single pass.
# Time  : O(n²)
# Space : O(n²)
from collections import defaultdict

class Solution2:
    def isValidSudoku(self, board):
        cols = defaultdict(set)                             # tracking digits in each column
        rows = defaultdict(set)                             # tracking digits in each row
        squares = defaultdict(set)                          # tracking digits in each 3 x 3 box (key = (r // 3, c // 3))

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                val = board[r][c]

                # Checking if the digit already exists in row, column or box
                # row[r], cols[c],squares[..] create new defaultdict() dynamically as needed
                if val in rows[r] or val in cols[c] or val in squares[(r // 3, c // 3)]:    # 9 cells will have same coordinates across 9 boxes.
                    return False                            # duplicate found

                # Recording the unseen digit in each structure
                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)          # cell level addition into each boxes

        return True                                         # valid board
    

# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Bitmask
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Represent seen digits as bits in 9 integers (one for each row, col, box). 0|0=0, 0|1=1, 1|1=1, 0&0=0, 0&1=0, 1&1=1
# Time  : O(n²)
# Space : O(n)
class Solution3:
    def isValidSudoku(self, board):
        rows = [0] * 9                                  # Bitmask to track digits seen in each row
        cols = [0] * 9                                  # Bitmask to track digits seen in each column
        squares = [0] * 9                               # Bitmask to track digits seen in each 3 x 3 sub-box

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue                            # Skipping empty cell

                val = int(board[r][c]) - 1              # Converting char to 0-based digit, i.e. 1-9 -> 0-8
                bit = 1 << val                          # Creating bitmask for digit, by shifting '1' val-times to the left e.g. 1 << 3 -> 00001000 -> 2^3 = 8
                box_index = (r // 3) * 3 + (c // 3)     # Determining which 3 x 3 box we're in

                # Checking for conflicts in row, column or box
                if (bit & rows[r]) or (bit & cols[c]) or (bit & squares[box_index]):    # 00100000 & 00100010 = 00100000 = True (match detected)
                    return False                        # duplicate found

                # Marking digit (adding/OR-ing new bit) as seen in each structure
                rows[r] |= bit                          # 00010000 | 00000010 = 00010010
                cols[c] |= bit
                squares[box_index] |= bit

        return True                                     # valid board
    


def main():
    board = [["1","2",".",".","3",".",".",".","."], 
             ["4",".",".","5",".",".",".",".","."],
             [".","9","8",".",".",".",".",".","3"],
             ["5",".",".",".","6",".",".",".","4"],
             [".",".",".","8",".","3",".",".","5"],
             ["7",".",".",".","2",".",".",".","6"],
             [".",".",".",".",".",".","2",".","."],
             [".",".",".","4","1","9",".",".","8"],
             [".",".",".",".","8",".",".","7","9"]]
    sln1 = Solution1()
    print(sln1.isValidSudoku(board))
    sln2 = Solution2()
    print(sln2.isValidSudoku(board))
    sln3 = Solution3()
    print(sln3.isValidSudoku(board))


if __name__ == "__main__":
    main()