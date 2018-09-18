class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        ret = [0] * (len(triangle) + 1)
        for i in range(len(triangle)-1, -1, -1):
            for j in range(len(triangle[i])):
                ret[j] = min(ret[j], ret[j+1]) + triangle[i][j]
        return ret[0]

if __name__ == "__main__":
    Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])