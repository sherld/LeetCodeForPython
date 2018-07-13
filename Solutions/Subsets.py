class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        flag = [False for i in range(len(nums))]
        ret = []
        stack = []
        self.dfs(nums, ret, flag, stack, 0)
        return ret
    
    def dfs(self, nums, ret, flag, stack, idx):
        ret.append(list(stack))
        for i in range(idx, len(nums)):
            if flag[i] == True:
                continue
            flag[i] = True
            stack.append(nums[i])
            self.dfs(nums, ret, flag, stack, i+1)
            stack.pop()
            flag[i] = False

