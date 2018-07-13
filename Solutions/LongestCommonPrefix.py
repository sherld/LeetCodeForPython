class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ''
        minLen = len(strs[0])
        for s in strs:
            minLen = min(minLen, len(s))
        
        comStr = ''
        for i in range(minLen):
            char = strs[0][i]
            for string in strs:
                if string[i] != char:
                    return comStr
            comStr += char
        return comStr

        
        
if __name__ == '__main__':
    strs = ['asdf','aswe','asre']
    print(Solution().longestCommonPrefix(strs))