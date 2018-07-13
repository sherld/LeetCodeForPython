class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        charMap = {}
        for v in t:
            charMap[v] = charMap.get(v, 0) + 1
        
        left = 0
        right = 0
        minLen = len(s) + 1
        minStart = 0
        count = 0
        for right in range(len(s)):
            if s[right] in charMap:
                charMap[s[right]] = charMap[s[right]] - 1
                if charMap[s[right]] >= 0:
                    count += 1
                while count == len(t):
                    if right - left + 1 < minLen:
                        minLen = right - left + 1
                        minStart = left
                    if s[left] in charMap:
                        charMap[s[left]] = charMap[s[left]] + 1
                        if charMap[s[left]] > 0:
                            count -= 1
                    left += 1
        if minLen > len(s):
            return ""
        return s[minStart:minStart+minLen]

if __name__ == "__main__":
    Solution().minWindow("ADOBECODEBANC", "ABC")