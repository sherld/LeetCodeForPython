class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        shift = k % len(nums)
        self.reverseNums(nums, 0, len(nums)-1)
        self.reverseNums(nums, 0, shift-1)
        self.reverseNums(nums, shift, len(nums)-1)
    
    def reverseNums(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
