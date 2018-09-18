class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        nums = [0] * (n+1)
        nums[0] = 1
        nums[1] = 1
        for i in range(2,n+1):
            for j in range(i):
                nums[i] += nums[j] * nums[i-1-j]
        return nums[n]