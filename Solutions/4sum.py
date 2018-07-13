class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        sortedNums = sorted(nums)
        ret = set()
        maxVal = sortedNums[-1]
        for i in range(len(sortedNums)):
            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue
            if sortedNums[i] + 3*maxVal < target:
                continue
            if 4*sortedNums[i] > target:
                break
            for j in range(i+1, len(sortedNums)):
                k = j + 1
                l = len(sortedNums) - 1
                while k < l:
                    if sortedNums[i] + sortedNums[j] + sortedNums[k] + sortedNums[l] < target:
                        k += 1
                    elif sortedNums[i] + sortedNums[j] + sortedNums[k] + sortedNums[l] > target:
                        l -= 1
                    else:
                        ret.add((sortedNums[i],sortedNums[j],sortedNums[k],sortedNums[l]))
                        k += 1
                        l -= 1
        return list(ret)

if __name__ == '__main__':
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))