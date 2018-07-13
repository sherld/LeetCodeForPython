class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        stack = []
        candidates.sort()
        self.findCombination(ret, candidates, stack, target, 0)
        return ret
    
    def findCombination(self, ret, candidates, stack, target, idx):
        if target < 0:
            return
        if target == 0:
            ret.append(list(stack))
        for i in range(idx, len(candidates)):
            stack.append(candidates[i])
            self.findCombination(ret, candidates, stack, target - candidates[i], i)
            stack.pop()

if __name__ == '__main__':
    print(Solution().combinationSum([2,3,6,7], 7))