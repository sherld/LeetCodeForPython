class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ret = []
        self.dfs(s, 0, ret, [])
        return ret
    
    def dfs(self, s, p, ret, stack):
        if p >= len(s):
            ret.append(list(stack))
            return
        for i in range(p, len(s)):
            if self.isPalindrome(s, p, i):
                stack.append(s[p:i+1])
                self.dfs(s, i+1, ret, stack)
                stack.pop()
    
    def isPalindrome(self, s, l, r):
        if l == r:
            return True
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

if __name__ == '__main__':
    Solution().partition("aab")