class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if not nums and len(nums) == 0:
            return -1
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[mid] > nums[right]:
                    if nums[left] <= target:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] < target:
                if nums[mid] < nums[left]:
                    if nums[right] >= target:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    left = mid + 1
        return -1

if __name__ == '__main__':
    print(Solution().search([3,5,1], 3))