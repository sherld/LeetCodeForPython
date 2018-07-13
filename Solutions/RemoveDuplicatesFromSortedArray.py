class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        head = 0
        tail = 1
        while tail < len(nums):
            if nums[tail] != nums[tail - 1]:
                head += 1
                nums[head] = nums[tail]
            tail += 1
        return head + 1

if __name__ == '__main__':
    print(Solution().removeDuplicates([1,1,2]))