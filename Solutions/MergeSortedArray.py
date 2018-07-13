class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        for i in range(m+n-1,-1,-1):
            if p1 < 0:
                nums1[i] = nums2[p2]
                p2 -= 1
            elif p2 < 0:
                return
            elif nums1[p1] < nums2[p2]:
                nums1[i] = nums2[p2]
                p2 -= 1
            else:
                nums1[i] = nums1[p1]
                p1 -= 1

if __name__ == "__main__":
    Solution().merge([1,2,3,0,0,0],3,[2,5,6],3)