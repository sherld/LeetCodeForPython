class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        sort_nums = sorted(nums)
        self.dfs(sort_nums, ret, [], 0)
        return ret
    
    def dfs(self, nums, ret, stack, p):
        ret.append(list(stack))
        for i in range(p, len(nums)):
            if i > p and nums[i] == nums[i-1]:
                continue
            stack.append(nums[i])
            self.dfs(nums, ret, stack, i + 1)
            stack.pop()

if __name__ == "__main__":
    Solution().subsetsWithDup([1,2,2])