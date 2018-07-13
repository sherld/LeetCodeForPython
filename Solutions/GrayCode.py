class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = []
        ret.append(0)
        for i in range(n):
            size = len(ret)
            for k in range(size-1, -1, -1):
                ret.append(ret[k] | 1 << i)
        return ret