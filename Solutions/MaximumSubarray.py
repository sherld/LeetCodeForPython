class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxValue = nums[0]
        ret = nums[0]
        for i in range(1, len(nums)):
            maxValue = max(maxValue + nums[i], nums[i])
            ret = max(maxValue, ret)
        return ret

if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))