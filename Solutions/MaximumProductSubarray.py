import math

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = nums[0]
        minVal = nums[0]
        ret = nums[0]
        for i in range(1,len(nums)):
            maxVal, minVal = max(nums[i], nums[i]*maxVal, nums[i]*minVal), min(nums[i], nums[i]*maxVal, nums[i]*minVal)
            ret = max(maxVal, ret)
        return ret

if __name__ == "__main__":
    print(Solution().maxProduct([2,0,1]))