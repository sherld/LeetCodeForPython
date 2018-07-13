class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rowLen = len(obstacleGrid)
        columnLen = len(obstacleGrid[0])

        nums = [0 for i in range(columnLen)]
        p = 0
        while p < columnLen and obstacleGrid[0][p] == 0:
            nums[p] = 1
            p += 1
        for i in range(1, rowLen):
            if obstacleGrid[i][0] == 1:
                nums[0] = 0
            for j in range(1, columnLen):
                if obstacleGrid[i][j] == 1:
                    nums[j] = 0
                else:
                    nums[j] = nums[j] + nums[j-1]
        return nums[columnLen-1]

if __name__ == '__main__':
    Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])