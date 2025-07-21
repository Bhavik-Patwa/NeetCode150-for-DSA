# Problem 4.2 - Search in a 2D Matrix
# Search for a target in a sorted array of distinct integers. Return its index or -1 if not found.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Check every element in the matrix one by one.
# Time  : O(m * n)
# Space : O(1)
class Solution1:
    def searchMatrix(self, matrix, target):
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == target:              # Checking each cell
                    return True
        return False                                    # Returning False if not found
    

# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Staircase Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Start from top-right corner; move left if too big, down if too small.
# Time  : O(m + n)
# Space : O(1)
class Solution2:
    def searchMatrix(self, matrix, target):             
        m, n = len(matrix), len(matrix[0])              # len(matrix) : rows, len(matrix[0] : columns
        r, c = 0, n - 1                                 # Starting at top-right

        while r < m and c >= 0:
            if matrix[r][c] > target:
                c -= 1                                  # Moving left
            elif matrix[r][c] < target:
                r += 1                                  # Moving down
            else:
                return True                             # Target found
        return False                                    # Not found


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Binary Search (Two Pass)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : First find potential row with binary search, then search that row.
# Time  : O(log m + log n)
# Space : O(1)
class Solution3:
    def searchMatrix(self, matrix, target):
        ROWS, COLS = len(matrix), len(matrix[0])    # len(matrix) : rows, len(matrix[0] : columns

        top, bot = 0, ROWS - 1                      # Binary search to find the correct row
        while top <= bot:
            row = (top + bot) // 2
            if target < matrix[row][0]:             # Less than first element of row
                bot = row - 1                       # Moving to rows above
            elif target > matrix[row][-1]:          # Greater than last element of row
                top = row + 1                       # Moving to rows below
            else:
                break                               # Target may exist in this row

        if not (top <= bot):
            return False                            # Valid row not found

        row = (top + bot) // 2                      # Recomputing row after loop

        l, r = 0, COLS - 1                          # Binary search within the identified row
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1                           # Moving right
            elif target < matrix[row][m]:
                r = m - 1                           # Moving left
            else:
                return True                         # Target found
        return False                                # Not found in row


# ---------------------------------------------------------------------------------------------------------------------------------------
# 4. Binary Search (One Pass)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Treat the matrix as a flat array and perform one binary search.
# Time  : O(log(m * n))
# Space : O(1)
class Solution4:
    def searchMatrix(self, matrix, target):
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1               # Searching in 1D index space
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS      # Mapping back to 2D indices

            if target > matrix[row][col]:
                l = m + 1                       # Moving right
            elif target < matrix[row][col]:
                r = m - 1                       # Moving left
            else:
                return True                     # Target found
        return False                            # Target not found



def main():
    matrix = [[1, 2, 4, 8], 
              [10, 11, 12, 13], 
              [14, 20, 30, 40]]
    target = 10
    for i in range(len(matrix)):
        print(matrix[i])
    print(Solution1().searchMatrix(matrix, target))
    print(Solution2().searchMatrix(matrix, target))
    print(Solution3().searchMatrix(matrix, target))
    print(Solution4().searchMatrix(matrix, target))


if __name__ == '__main__':
    main()