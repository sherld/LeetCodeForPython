class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == "0":
            return 0
        x = 1
        y = 1
        for i in range(1, len(s)):
            if s[i] == "0":
                if s[i-1] == "0" or int(s[i-1]) > 2:
                    return 0
                sum = x
            elif s[i-1] == "1" or (s[i-1] == "2" and int(s[i]) <= 6):
                sum = x + y
            else:
                sum = y
            x = y
            y = sum
        return y

if __name__ == "__main__":
    Solution().numDecodings("12")