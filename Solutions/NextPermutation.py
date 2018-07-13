class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        idx = len(nums) - 2
        while idx >= 0 and nums[idx] >= nums[idx + 1]:
            idx -= 1
        if idx >= 0:
            biggerIdx = idx + 1
            while biggerIdx < len(nums) and nums[biggerIdx] > nums[idx]:
                biggerIdx += 1
            tmp = nums[idx]
            nums[idx] = nums[biggerIdx - 1]
            nums[biggerIdx - 1] = tmp
        idx += 1
        tail = len(nums) - 1
        while idx < tail:
            tmp = nums[idx]
            nums[idx] = nums[tail]
            nums[tail] = tmp
            idx += 1
            tail -= 1

if __name__ == '__main__':
    Solution().nextPermutation([3,5,4,3,3,2])