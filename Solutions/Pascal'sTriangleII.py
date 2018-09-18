class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret = []
        for i in range(rowIndex+1):
            ret.insert(0, 1)
            for j in range(1, i):
                ret[j] = ret[j] + ret[j+1]
        return ret

if __name__ == '__main__':
    Solution().getRow(4)