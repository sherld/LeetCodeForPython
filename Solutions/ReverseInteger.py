import sys

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x >= 0 else -1
        x = abs(x)
        y = 0
        while x != 0:
            a = x % 10
            y = y * 10 + a
            x = x // 10
        return 0 if y > 2**31 else y*sign

if __name__ == "__main__":
    num = -123
    print(Solution().reverse(num))