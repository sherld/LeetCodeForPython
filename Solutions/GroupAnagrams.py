class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sortedStrs = list(map(lambda item : ''.join(sorted(item)), strs))
        strMap = {}
        for idx, val in enumerate(strs):
            if sortedStrs[idx] in strMap:
                strMap[sortedStrs[idx]].append(val)
            else:
                strMap[sortedStrs[idx]] = [val]
        return list(strMap.values())

if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))