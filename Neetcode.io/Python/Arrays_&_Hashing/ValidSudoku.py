#! https://leetcode.com/problems/valid-sudoku/
"""
36. Valid Sudoku
Medium
9.8K
1K
Companies
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:


Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""
class Solution(object):
    def isValidSudokuBruteForce(self, board):
        """
        Determines if a 9x9 Sudoku board is valid according to the following rules:
        - Each row must contain the digits 1-9 without repetition.
        - Each column must contain the digits 1-9 without repetition.
        - Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

        :param board: List[List[str]] - The input Sudoku board, represented as a 2D list of strings.
        :return: bool - True if the Sudoku board is valid, False otherwise.

        Algorithm:
        1. Check if each row contains unique values:
           - Create a dictionary `row_values_dict` to store the count of each value in the row.
           - Iterate over each cell in the row:
             - If the cell value is not ".", check if it already exists in `row_values_dict`.
               - If it exists, return False.
               - Otherwise, add it to `row_values_dict`.
        2. Check if each column contains unique values:
           - Create a dictionary `column_values_dict` to store the count of each value in the column.
           - Iterate over each cell in the column:
             - If the cell value is not ".", check if it already exists in `column_values_dict`.
               - If it exists, return False.
               - Otherwise, add it to `column_values_dict`.
        3. Check if each 3x3 block contains unique values:
           - Iterate over each block (3x3 sub-box):
             - Create a dictionary `block_values_dict` to store the count of each value in the block.
             - Iterate over each cell in the block:
               - Calculate the row and column indices of the cell based on the block indices.
               - If the cell value is not ".", check if it already exists in `block_values_dict`.
                 - If it exists, return False.
                 - Otherwise, add it to `block_values_dict`.
        4. If all checks pass, return True.

        Time complexity: O(1) (since the board is fixed size)
        Space complexity: O(1)
        """

        # Checking if row values are unique
        for i in range(len(board)):
            row_values_dict = {}
            for j in range(len(board)):
                if board[i][j] != ".":
                    if board[i][j] in row_values_dict:
                        return False
                    else:
                        row_values_dict[board[i][j]] = row_values_dict.get(board[i][j], 0) + 1

        # Checking if column values are unique
        for i in range(len(board)):
            column_values_dict = {}
            for j in range(len(board)):
                if board[j][i] != "." and board[j][i] in column_values_dict:
                    return False
                else:
                    column_values_dict[board[j][i]] = column_values_dict.get(board[j][i], 0) + 1

        # Checking if 3x3 block values are unique
        for block_row in range(3):
            for block_col in range(3):
                block_values_dict = {}
                for i in range(3):
                    for j in range(3):
                        # Calculate the row and column indices of the cell based on the block indices
                        row = 3 * block_row + i
                        col = 3 * block_col + j
                        if board[row][col] != ".":
                            if board[row][col] in block_values_dict:
                                return False
                            else:
                                block_values_dict[board[row][col]] = 1

        return True

    def isValidSudokuHashSet(self, board):
        """
        Determines if a 9x9 Sudoku board is valid according to the following rules:
        - Each row must contain the digits 1-9 without repetition.
        - Each column must contain the digits 1-9 without repetition.
        - Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

        :param board: List[List[str]] - The input Sudoku board, represented as a 2D list of strings.
        :return: bool - True if the Sudoku board is valid, False otherwise.

        Time complexity: O(1) (since the board is fixed size)
        Space complexity: O(1)
        """

        # Initialize sets to keep track of seen values in each row, column, and sub-grid
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    # Check if the value is already seen in the same row
                    if num in row_sets[i]:
                        return False
                    row_sets[i].add(num)

                    # Check if the value is already seen in the same column
                    if num in col_sets[j]:
                        return False
                    col_sets[j].add(num)

                    # Check if the value is already seen in the same sub-grid
                    subgrid_row = i // 3
                    subgrid_col = j // 3
                    if num in subgrid_sets[subgrid_row][subgrid_col]:
                        return False
                    subgrid_sets[subgrid_row][subgrid_col].add(num)

        return True
                    

            
obj = Solution()

board1 = [["5","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]]

board2 = [["8","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]]

print(obj.isValidSudokuBruteForce(board1))
print(obj.isValidSudokuBruteForce(board2))
print(obj.isValidSudokuHashSet(board1))
print(obj.isValidSudokuHashSet(board2))

