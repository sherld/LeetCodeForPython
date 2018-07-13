class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        head = 0
        tail = 1
        flag = False
        while tail < len(nums):
            if nums[tail] == nums[tail - 1]:
                if not flag:
                    flag = True
                    head += 1
                    nums[head] = nums[tail]
            else:
                flag = False
                head += 1
                nums[head] = nums[tail]
            tail += 1
        return head + 1