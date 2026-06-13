"""
LeetCode 0036 · Valid Sudoku  |  Arrays & Hashing  |  Medium
Time: O(n^2)  Space: O(n^2)

Problem:
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

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

Idea:
    Maintain three sets of seen values: one per row, one per column, and one per 3x3 box (indexed by r//3, c//3).
    For each filled cell, check if its value already exists in the corresponding row, column, or box set — if so,
    the board is invalid. Otherwise add it to all three sets and continue.
"""

from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in row[r]
                    or board[r][c] in col[c]
                    or board[r][c] in grid[(r // 3, c // 3)]
                ):
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                grid[(r // 3, c // 3)].add(board[r][c])
        return True
