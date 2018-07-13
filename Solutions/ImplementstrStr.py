class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if haystack == None or needle == None:
            return -1

        if not needle:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            j = 0
            while j < len(needle):
                if haystack[i + j] != needle[j]:
                    break
                j += 1
            if j == len(needle):
                return i
        return -1

if __name__ == '__main__':
    print(Solution().strStr("",""))
        