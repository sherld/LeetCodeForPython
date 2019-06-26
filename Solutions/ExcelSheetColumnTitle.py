class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        title = ''
        while n > 0:
            n -= 1
            title = chr(ord('A') + n % 26) + title
            n = n // 26
        return title

if __name__ == "__main__":
    print(Solution().convertToTitle(1))