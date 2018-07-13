class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rowLen = len(matrix)
        columnLen = len(matrix[0])

        # 这里可以借用第一行和第一列作为存放标志位，额外只需要两个参数
        rowRecord = [0] * rowLen
        columnRecord = [0] * columnLen
        for i in range(rowLen):
            for j in range(columnLen):
                if matrix[i][j] == 0:
                    rowRecord[i] = 1
                    columnRecord[j] = 1
        for k in range(rowLen):
            if rowRecord[k] == 1:
                for m in range(columnLen):
                    matrix[k][m] = 0
        for k in range(columnLen):
            if columnRecord[k] == 1:
                for n in range(rowLen):
                    matrix[n][k] = 0

if __name__ == "__main__":
    Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]])