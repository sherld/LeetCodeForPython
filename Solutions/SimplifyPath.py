import re

class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        pathList = re.split(r'/+', path)
        stack = []
        for v in pathList:
            if v == "..":
                if stack:
                    stack.pop()
            elif v != "" and v != ".":
                stack.append(v)
        if not stack:
            return "/"
        ret = ""
        for item in stack:
            ret += "/" + item
        return ret

if __name__ == '__main__':
    Solution().simplifyPath("/a/./b/../../c/")