class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = 0
        while n > 0:
            if n & 1 == 1:
                nums += 1
            n = n >> 1
        return nums