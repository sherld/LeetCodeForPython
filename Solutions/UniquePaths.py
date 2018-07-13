class Solution:
    def uniquePaths(self, m, n):
        nums = [1 for i in range(m)]
        for i in range(1, n):
            for j in range(1, m):
                nums[j] = nums[j] + nums[j-1]
        return nums[m-1]

    def uniquePathsMine(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        matrix = [[0 for j in range(m+1) ] for i in range(n)]
        matrix[0] = [1 for i in range(m+1)]
        for i in range(1, n):
            matrix[i][0] = 0
        for i in range(1, n):
            for j in range(1, m + 1):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[n-1][m]

if __name__ == "__main__":
    print(Solution().uniquePaths(3, 2))