from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board  # Create instance variable
        self.size = 9
        self.solve()

    def solve(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] != '.':
                    continue
                for num in range(1, 10):  # Try all possible combinations
                    if self.is_valid(row, col, str(num)):  # If comb is valid
                        self.board[row][col] = str(num)  # Make move
                        if self.solve():
                            return True  # Board is solving with move
                        else:
                            self.board[row][col] = '.'  # Reset and go back
                return False  # No combination valid, wrong moves so far
        return True  # Moves so far valid

    def is_valid(self, row: int, col: int, num: str) -> bool:
        for i in range(self.size):
            # Check row validity
            if self.board[i][col] != '.' and self.board[i][col] == num:
                return False
            # Check column validity
            if self.board[row][i] != '.' and self.board[row][i] == num:
                return False
            # Check box validity
            box = self.board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3]
            if box != '.' and box == num:
                return False
        return True
