class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        list1 = list(map(int, version1.split('.')))
        list2 = list(map(int, version2.split('.')))

        maxLen = max(len(list1), len(list2))
        if maxLen > len(list1):
            list1 += [0] * (maxLen - len(list1))
        if maxLen > len(list2):
            list2 += [0] * (maxLen - len(list2))
        for v1, v2 in zip(list1, list2):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0

if __name__ == "__main__":
    Solution().compareVersion("1.1", "1")