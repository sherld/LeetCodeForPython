class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        while lo < hi - 1:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] > nums[mid-1]:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo if nums[lo] >= nums[hi] else hi