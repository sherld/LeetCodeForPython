class Solution:
    def longestConsecutiveMine(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sortedNums = sorted(nums)
        maxLen = 1
        consecutiveLen = 1
        for i in range(1, len(sortedNums)):
            if sortedNums[i] - sortedNums[i-1] == 1:
                consecutiveLen += 1
                maxLen = max(maxLen, consecutiveLen)
            elif sortedNums[i] == sortedNums[i-1]:
                continue
            else:
                consecutiveLen = 1
        return maxLen
    
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak