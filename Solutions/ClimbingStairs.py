class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        x = 1
        y = 2
        for i in range(n - 2):
            z = x + y
            x = y
            y = z
        return z