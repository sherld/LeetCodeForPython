class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        sign = (dividend > 0) == (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        v = divisor
        count = 1
        ret = 0
        while v <= dividend:
            v = v << 1
            count = count << 1
        
        while count > 0:
            while dividend >= v:
                ret += count
                dividend = dividend - v
            v = v >> 1
            count = count >> 1
        return ret if sign else -ret



    def divideLowPerformance(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = (dividend > 0) == (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        if divisor == 0:
            return 0
        while dividend >= divisor:
            quotient += 1
            dividend -= divisor
        return quotient if sign else -quotient

if __name__ == '__main__':
    print(Solution().divide(2,1))