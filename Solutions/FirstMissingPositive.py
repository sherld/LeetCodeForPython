class Solution:
    def firstMissingPositiveBetter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 1

        i = 0
        while i < len(nums):
            if nums[i] - 1 >= 0 and nums[nums[i] - 1] != nums[i] and nums[i] - 1 < len(nums):
                tmp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = tmp
                i -= 1
            i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 1

        i = 0
        while i < len(nums):
            if nums[i] - 1 >= 0 and nums[i] != i + 1 and nums[i] - 1 < len(nums):
                if nums[nums[i] - 1] != nums[i]:
                    tmp = nums[nums[i] - 1]
                    nums[nums[i] - 1] = nums[i]
                    nums[i] = tmp
                    i -= 1
            i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

if __name__ == "__main__":
    print(Solution().firstMissingPositive([1,1]))