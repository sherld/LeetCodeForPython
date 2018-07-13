class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        mapping = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ret = []
        self.buildLetters(digits, 0, ret, "", mapping)
        return ret

    def buildLetters(self, digits, idx, ret, buildLetter, mapping):
        if idx >= len(digits):
            ret.append(buildLetter)
            return
        for char in mapping[int(digits[idx])]:
            buildLetter += char
            self.buildLetters(digits, idx+1, ret, buildLetter, mapping)
            buildLetter = buildLetter[0:len(buildLetter) - 1]
        

if __name__ == '__main__':
    print(Solution().letterCombinations("22"))