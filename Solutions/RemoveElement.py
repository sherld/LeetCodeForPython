class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        head = 0
        tail = 0
        while tail < len(nums):
            if nums[tail] != val:
                nums[head] = nums[tail]
                head += 1
            tail += 1
        return head
        
if __name__ == '__main__':
    nums = [1,2,3,3,4]
    Solution().removeElement(nums, 3)
    print(nums)