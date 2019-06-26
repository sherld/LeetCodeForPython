class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        ret = set()
        for i in range(len(s) - 9):
            if s[i:i+10] not in seen:
                seen.add(s[i:i+10])
            else:
                ret.add(s[i:i+10])
        return list(ret)