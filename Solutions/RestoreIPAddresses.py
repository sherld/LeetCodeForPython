class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []
        self.dfs(s, ret, [], 0)
        return map(lambda stack: stack.join(','), ret)
        

    def dfs(self, s, ret, stack, p):
        if (4 - len(stack)) * 3 < len(s) - p:
            return
        if p == len(s) and len(stack) == 4:
            return ret.append(list(stack))
        for i in range(3):
            if p + i > len(s):
                return
            subStr = s[p:p+i+1]
            if int(subStr) > 255:
                continue
            stack.append(subStr)
            self.dfs(s, ret, stack, p+i+1)
            stack.pop()

if __name__ == '__main__':
    Solution().restoreIpAddresses("25525511135")