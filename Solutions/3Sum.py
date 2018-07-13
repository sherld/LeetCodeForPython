class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        sortedNum = sorted(nums)
        ret = set()
        for i in range(len(sortedNum)):
            val = sortedNum[i]
            j = i + 1
            k = len(sortedNum) - 1
            while j < k:
                if sortedNum[j] + sortedNum[k] < -val:
                    j += 1
                elif sortedNum[j] + sortedNum[k] > -val:
                    k -= 1
                else:
                    ret.add((sortedNum[i], sortedNum[j], sortedNum[k]))
                    j += 1
                    k -= 1
            if val >= 0:
                break
        return list(ret)

    
if __name__ == '__main__':
    array = [-1,0,1,2,-1,-4]
    print(Solution().threeSum(array))