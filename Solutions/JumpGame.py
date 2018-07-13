class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        maxDist = 0
        for i in range(len(nums)):
            if i > maxDist:
                return False
            dist = i + nums[i]
            maxDist = max(maxDist, dist)
        return True

if __name__ == '__main__':
    print(Solution().canJump([2,3,1,1,4]))