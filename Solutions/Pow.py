class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        flag = True if n > 0 else False
        count = abs(n)
        tmp = x
        ret = 1
        while count != 0:
            if count % 2 == 1:
                ret *= tmp
            tmp = tmp * tmp
            count = count // 2
        return ret if flag else 1/ret

if __name__ == '__main__':
    print(Solution().myPow(2, -2))