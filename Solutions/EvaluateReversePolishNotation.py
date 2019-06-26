class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif token == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif token == '/':
                # here take care of the case like "1/-22",
                # in Python 2.x, it returns -1, while in 
                # Leetcode it should return 0
                a = stack.pop()
                b = stack.pop()
                if b*a < 0 and b % a != 0:
                    stack.append(b//a+1)
                else:
                    stack.append(b//a)
            elif token == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            else:
                stack.append(int(token))
        return stack[0]

if __name__ == "__main__":
    Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])