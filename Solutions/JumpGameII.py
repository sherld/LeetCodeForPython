class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        dest = [i + v for i, v in enumerate(nums)]
        lo = 1
        hi = nums[0]
        step = 1
        while hi < len(nums) - 1:
            maxDistIdx = lo
            for i in range(lo, hi + 1):
                if dest[i] > dest[maxDistIdx]:
                    maxDistIdx = i
            lo = hi + 1
            hi = dest[maxDistIdx]
            step += 1
        return step

    def jumpInJava(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums == None or len(nums) == 0:
            return 0
        lastReach = 0
        reach = 0
        step = 0
        for i in range(0, len(nums)):
            if i > reach:
                break
            if i > lastReach:
                step += 1
                lastReach = reach
            reach = max(reach, nums[i] + i)
        if reach < len(nums) - 1:
            return 0
        return step

    def jumpLowPerformance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        minStep = [len(nums) for i in range(len(nums))]
        minStep[0] = 0
        for i in range(len(nums)):
            val = nums[i]
            for j in range(i + 1, min(i + val + 1, len(nums))):
                minStep[j] = min(minStep[j], minStep[i] + 1)
        return minStep[-1]

if __name__ == '__main__':
    print(Solution().jump([5,9,3,2,1,0,2,3,3,1,0,0]))