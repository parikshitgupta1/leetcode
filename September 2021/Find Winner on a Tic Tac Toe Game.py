from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        rows, cols = [0] * n, [0] * n
        diag = anti_diag = 0
        player = 1

        for row, col in moves:
            rows[row] += player
            cols[col] += player
            if row == col:
                diag += player
            if row + col == n - 1:
                anti_diag += player
            if any(abs(line) == n for line in (rows[row], cols[col], diag, anti_diag)):
                return "A" if player == 1 else "B"
            player *= -1
        return "Draw" if len(moves) == n * n else "Pending"
