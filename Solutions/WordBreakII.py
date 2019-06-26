class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.dfs(s, wordDict, {})
    
    def dfs(self, s, wordDict, wordMap):
        if not s:
            return [""]
        if s in wordMap:
            return wordMap[s]
        ret = []
        for word in wordDict:
            if s.startswith(word):
                subList = self.dfs(s[len(word):], wordDict, wordMap)
                for item in subList:
                    ret.append(word + (" " if item else '') + item)
        wordMap[s] = ret
        return ret

if __name__ == '__main__':
    Solution().wordBreak("catsanddog",["cat","cats","and","sand","dog"])