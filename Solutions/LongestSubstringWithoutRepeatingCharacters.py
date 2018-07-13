class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pMap = {}
        longestLen = 0
        startIdx = 0
        for curidx, val in enumerate(s):
            if val in pMap:
                lastIdx = pMap[val]
                if lastIdx >= startIdx:
                    longestLen = max(longestLen, curidx - startIdx)
                    startIdx = lastIdx + 1
                else:
                    longestLen = max(longestLen, curidx - startIdx)
            pMap[val] = curidx
        return max(longestLen, len(s) - startIdx)


if __name__ == '__main__':
    s = "bcbrtyu"
    print(Solution().lengthOfLongestSubstring(s))