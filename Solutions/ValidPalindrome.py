class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        head = 0
        tail = len(s) - 1
        while head < tail:
            while head < len(s) and not s[head].isalnum():
                head += 1
            while tail >= 0 and not s[tail].isalnum():
                tail -= 1
            if head >= tail or head >= len(s) or tail < 0:
                return True
            if s[head].lower() != s[tail].lower():
                return False
            head += 1
            tail -= 1
        return True

if __name__ == "__main__":
    Solution().isPalindrome('.,')