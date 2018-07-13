class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        flag = [False for i in range(len(nums))]
        ret = []
        dList = []
        self.dps(nums, ret, flag, dList)
        return ret

    def dps(self, nums, ret, flag, dList):
        if len(dList) == len(nums):
            ret.append(list(dList))
        for i in range(len(nums)):
            if not flag[i]:
                flag[i] = True
                dList.append(nums[i])
                self.dps(nums, ret, flag, dList)
                dList.pop()