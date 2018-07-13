class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        lo = 0
        hi = len(height) - 1
        left_max = 0
        right_max = 0
        ret = 0
        while lo < hi:
            if height[lo] <= height[hi]:
                if height[lo] > left_max:
                    left_max = height[lo]
                else:
                    ret += left_max - height[lo]
                lo += 1
            else:
                if height[hi] > right_max:
                    right_max = height[hi]
                else:
                    ret += right_max - height[hi]
                hi -= 1
        return ret

    def trapPerformanceIssue(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        maxHeight = max(height)
        size = 0

        for h in range(1, maxHeight + 1):
            container = list(map(lambda x : 1 if x >= h else 0, height))
            start = 0
            end = len(height) - 1
            while start < len(height) and container[start] == 0:
                start += 1
            while end >= 0 and container[end] == 0:
                end -= 1
            size += container[start:end + 1].count(0)
        return size

if __name__ == '__main__':
    print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))