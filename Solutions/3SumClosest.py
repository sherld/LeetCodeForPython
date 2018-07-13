import sys
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        sortedNums = sorted(nums)
        closestDiffValue = sys.maxsize
        closestVal = sys.maxsize
        for i in range(len(sortedNums)):
            val = sortedNums[i]
            j = i + 1
            k = len(sortedNums) - 1
            while j < k:
                diffVal = target - val - sortedNums[j] - sortedNums[k]
                if abs(diffVal) < closestDiffValue:
                    closestVal = val + sortedNums[j] + sortedNums[k]
                    closestDiffValue = abs(diffVal)
                if diffVal > 0:
                    j += 1
                elif diffVal < 0:
                    k -= 1
                else:
                    return target
        return closestVal

        
    

if __name__ == '__main__':
    array = [-1,0,1,1,55]
    print(Solution().threeSumClosest(array, 3))