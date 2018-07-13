class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        
        maxLen = 0
        idx = len(s) - 1
        while idx >= 0:
            if s[idx] != ' ':
                break
            idx -= 1
        while idx >= 0:
            if s[idx] == ' ':
                return maxLen
            else:
                maxLen += 1
            idx -= 1
        return maxLen