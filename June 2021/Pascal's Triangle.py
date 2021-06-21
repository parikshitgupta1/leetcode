class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]  # Initial Row
        for i in range(1, numRows):
            row = list()
            row.append(1)  # Starting 1
            for j in range(1, len(result[i-1])):
                # Addition of previous row numbers
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)  # Ending 1
            result.append(row)
        return result
