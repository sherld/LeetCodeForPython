class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        numList = [1]
        ret = []
        for i in range(numRows):
            ret.append(list(numList))
            numList.append(0)
            numList.insert(0, 0)
            newList = []
            for idx in range(len(numList)-1):
                newList.append(numList[idx] + numList[idx+1])
            numList = newList
        return ret

if __name__ == "__main__":
    Solution().generate(5)
