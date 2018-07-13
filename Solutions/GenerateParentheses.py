class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        ret = []
        self.buildParenthesis(ret, '', 0, n)
        return ret
    
    def buildParenthesis(self, ret, s, existedNum, remainNum):
        if existedNum == 0 and remainNum == 0:
            ret.append(s)
            return
        if remainNum > 0:
            self.buildParenthesis(ret, s + '(', existedNum + 1, remainNum - 1)
        if existedNum > 0:
            self.buildParenthesis(ret, s + ')', existedNum - 1, remainNum)



if __name__ == '__main__':
    print(Solution().generateParenthesis(3))