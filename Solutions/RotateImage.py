import math

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        n = length // 2
        for i in range(n):
            for j in range(i, length - 1 - i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[length-1-j][i]
                matrix[length-1-j][i] = matrix[length-1-i][length-1-j]
                matrix[length-1-i][length-1-j] = matrix[j][length-1-i]
                matrix[j][length-1-i] = temp

if __name__ == '__main__':
    matrix = [[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]
    Solution().rotate(matrix)
    print(matrix)