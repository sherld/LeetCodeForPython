class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.sort(nums, 0, len(nums)-1)
    
    def sort(self, nums, lo, hi):
        if lo >= hi:
            return
        lt = lo
        gt = hi
        i = lo
        v = nums[lo]
        while i <= gt:
            if nums[i] < v:
                tmp = nums[i]
                nums[i] = nums[lt]
                nums[lt] = tmp
                lt += 1
                i += 1
            elif nums[i] > v:
                tmp = nums[i]
                nums[i] = nums[gt]
                nums[gt] = tmp
                gt -= 1
            else:
                i += 1
        self.sort(nums, lo, lt - 1)
        self.sort(nums, gt + 1, hi)

if __name__ == "__main__":
    Solution().sortColors([2,0,2,1,1,0])