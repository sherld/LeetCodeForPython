class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexMap = {}
        for index, item in enumerate(nums):
            if item in indexMap:
                return [indexMap[item], index]
            indexMap[target-item] = index
        return []

 
if __name__ == '__main__':
    nums = [1,2,3,4]
    target = 4
    print(Solution.twoSum(nums, target))