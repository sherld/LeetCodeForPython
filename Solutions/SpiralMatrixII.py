class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        num = 1
        ret = [[0 for i in range(n)] for i in range(n)]
        for i in range(n // 2):
            for j in range(i, n - 1 - i):
                ret[i][j] = num
                num += 1
            for j in range(i, n - 1 - i):
                ret[j][n-1-i] = num
                num += 1
            for j in range(n - 1 - i, i, -1):
                ret[n-1-i][j] = num
                num += 1
            for j in range(n - 1 - i, i, -1):
                ret[j][i] = num
                num += 1
        if n % 2 == 1:
            mid = n // 2
            ret[mid][mid] = num
        return ret

if __name__ == '__main__':
    print(Solution().generateMatrix(3))