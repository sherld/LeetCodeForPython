class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        for val in s:
            if val == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif val == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif val == '}':
                if stack and stack[-1] == '{':
                        stack.pop()
                else:
                    return False
            else:
                stack.append(val)
        if stack:
            return False
        return True

        
if __name__ == '__main__':
    print(Solution().isValid('['))