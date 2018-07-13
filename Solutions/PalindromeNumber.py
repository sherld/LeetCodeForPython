class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        len = 0
        y = x
        while y > 0:
            y = y // 10
            len += 1
        while len >= 2:
            end = x % 10
            start = x // 10 ** (len - 1)
            if start != end:
                return False
            x = x % 10 ** (len - 1)
            x = x // 10
            len = len - 2
        return True

if __name__ == '__main__':
    print(Solution().isPalindrome(123321))