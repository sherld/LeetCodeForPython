class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        ret = '1'
        for i in range(n-1):
            ret = self.generateNewOne(ret)
        return ret
    
    def generateNewOne(self, s):
        ret = ""
        remain = s[len(s)-1]
        cnt = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == remain:
                cnt += 1
            else:
                ret = "%d%s%s" % (cnt, remain, ret)
                cnt = 1
                remain = s[i]
            
            if i == 0:
                ret = "%d%s%s" % (cnt, remain, ret)
        return ret

if __name__ == '__main__':
    print(Solution().generateNewOne('1211'))
            
