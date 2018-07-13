class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sortedNums = sorted(nums)
        stack = []
        ret = []
        flag = [False for i in range(len(sortedNums))]
        self.dps(sortedNums, ret, stack, flag)
        return ret

    def dps(self, sortedNums, ret, stack, flag):
        if len(stack) == len(sortedNums):
            ret.append(list(stack))
            return
        for i in range(len(sortedNums)):
            if flag[i]:
                continue
            if i > 0 and not flag[i-1] and sortedNums[i] == sortedNums[i-1]:
                continue
            flag[i] = True
            stack.append(sortedNums[i])
            self.dps(sortedNums, ret, stack, flag)
            stack.pop()
            flag[i] = False

if __name__ == '__main__':
    print(Solution().permuteUnique([1,1,1,2,2,3]))