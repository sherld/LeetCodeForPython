class Solution:
    # 可以用一维数组来实现
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1) + 1
        len2 = len(word2) + 1

        dp = [[0 for i in range(len1)] for j in range(len2) ]
        for i in range(len1):
            dp[0][i] = i
        for j in range(len2):
            dp[j][0] = j
        
        for x in range(1, len2):
            for y in range(1, len1):
                if word2[x-1] == word1[y-1]:
                    dp[x][y] = dp[x-1][y-1]
                else:
                    dp[x][y] = min(dp[x-1][y-1], dp[x-1][y], dp[x][y-1]) + 1
        return dp[len2-1][len1-1]

if __name__ == "__main__":
    Solution().minDistance("horse", "ros")