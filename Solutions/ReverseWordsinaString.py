import re
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        trimStr = s.strip()
        return " ".join(re.split(' +', trimStr)[::-1])

if __name__ == "__main__":
    print(Solution().reverseWords("the sky is blue"))