class Solution:
    def longestValidParenthesesBetter(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxNum = 0
        stack = []
        stack.append(-1)
        for idx, val in enumerate(s):
            if val == '(':
                stack.append(idx)
            else:
                stack.pop()
                if not stack:
                    stack.append(idx)
                else:
                    maxNum = max(maxNum, idx - stack[-1])
        return maxNum

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        maxNum = 0
        start = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        rightOne = stack[-1]
                        maxNum = max(maxNum, i - rightOne)
                    else:
                        maxNum = max(maxNum, i - start + 1)
                else:
                    maxNum = max(maxNum, i - start)
                    start = i + 1
        return maxNum

if __name__ == '__main__':
    print(Solution().longestValidParentheses("()()(()"))