class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxVals = [0] * len(nums)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        maxVals[0] = nums[0]
        maxVals[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            maxVals[i] = max(maxVals[i-2] + nums[i], maxVals[i-1])
        return maxVals[-1]
        

    def robRecursion(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = [0] * len(nums)
        return self.dfs(nums, memo, 0)
    
    def dfs(self, nums, memo, p):
        if p >= len(nums):
            return 0
        if memo[p] > 0:
            return memo[p]
        memo[p] = max(self.dfs(nums, memo, p+2) + nums[p], self.dfs(nums, memo, p+1))
        return memo[p]

if __name__ == "__main__":
    Solution().rob([2,7,9,3,1])