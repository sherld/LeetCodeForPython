class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        rowLen = len(grid)
        columnLen = len(grid[0])

        dp = [0 for i in range(columnLen)]

        for i in range(columnLen):
            if i == 0:
                dp[i] = grid[0][0]
            else:
                dp[i] = dp[i-1] + grid[0][i]
        
        for i in range(1, rowLen):
            for j in range(columnLen):
                if j == 0:
                    dp[0] = dp[0] + grid[i][0]
                else:
                    dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        return dp[columnLen - 1]

if __name__ == "__main__":
    Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]])