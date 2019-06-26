class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for i in range(len(s)):
            char = s[i]
            num = ord(char) - ord('A') + 1 + 26 * num
        return num