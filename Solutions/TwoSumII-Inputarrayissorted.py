class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo = 0
        hi = len(numbers) - 1
        while lo < hi:
            sum = numbers[lo] + numbers[hi]
            if sum < target:
                lo += 1
            elif sum > target:
                hi -= 1
            else:
                return [lo+1, hi+1]
        return None