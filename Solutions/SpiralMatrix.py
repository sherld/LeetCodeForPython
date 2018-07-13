class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        row = len(matrix)
        if row == 0:
            return ret
        column = len(matrix[0])
        if column == 0:
            return ret

        n = min(row, column)
        for i in range(n // 2):
            for j in range(i, column - i - 1):
                ret.append(matrix[i][j])
            for j in range(i, row - i - 1):
                ret.append(matrix[j][column-i-1])
            for j in range(column - i - 1, i, -1):
                ret.append(matrix[row-i-1][j])
            for j in range(row - i - 1, i, -1):
                ret.append(matrix[j][i])
        if n % 2 == 1:
            p = n // 2
            if row <= column:
                for i in range(p, column - p):
                    ret.append(matrix[p][i])
            else:
                for i in range(p, row - p):
                    ret.append(matrix[i][p])
        return ret

if __name__ == '__main__':
    print(Solution().spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]))