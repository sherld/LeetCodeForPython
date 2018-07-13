class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longestStr = ''
        length = len(s)
        for idx, val in enumerate(s):
            leftIdx = idx
            rightIdx = idx
            while leftIdx >= 0 and rightIdx <= length -1:
                if s[leftIdx] != s[rightIdx]:
                    break
                subStr = s[leftIdx:rightIdx+1]
                if len(subStr) > len(longestStr):
                    longestStr = subStr
                leftIdx -= 1
                rightIdx += 1
            leftIdx = idx
            rightIdx = idx + 1
            while leftIdx >= 0 and rightIdx <= length -1:
                if s[leftIdx] != s[rightIdx]:
                    break
                subStr = s[leftIdx:rightIdx+1]
                if len(subStr) > len(longestStr):
                    longestStr = subStr
                leftIdx -= 1
                rightIdx += 1
        return longestStr

    # a better one
    def longestPalindrome2(self, s):
        start = 0
        end = 0
        for idx, val in enumerate(s):
            len1 = self.expandAroundCenter(s, idx, idx)
            len2 = self.expandAroundCenter(s, idx, idx+1)
            length = max(len1, len2)
            if length > end - start:
                start = idx - (length - 1) / 2
                end = idx + length / 2
        return s[start:end+1]

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

        
if __name__ == '__main__':
    s = "babad"
    print(Solution().longestPalindrome(s))