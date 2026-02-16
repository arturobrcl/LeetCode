class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [[1 for _ in range(_)] for _ in range(1, rowIndex + 2)]
        if rowIndex < 2:
            return pascal[rowIndex]
        else:
            for i in range(2, rowIndex + 1):
                for j in range(1, i):
                    pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

        return pascal[rowIndex]
