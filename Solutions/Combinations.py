class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [i+1 for i in range(n)]
        flag = [False for i in range(n)]
        ret = []
        self.dfs(ret, nums, flag, [], k, 0)
        return ret
    
    def dfs(self, ret, nums, flag, stack, count, p):
        if count == 0:
            ret.append(list(stack))
            return
        if p >= len(nums):
            return
        for i in range(p, len(nums)):
            if flag[i]:
                continue
            flag[i] = True
            stack.append(nums[i])
            self.dfs(ret, nums, flag, stack, count-1, i+1)
            stack.pop()
            flag[i] = False

if __name__ == "__main__":
    Solution().combine(4,2)