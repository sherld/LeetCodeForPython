class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        maxWater = 0
        while start < end:
            width = min(height[start], height[end])
            maxWater = max(maxWater, width * (end - start))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return maxWater
        
if __name__ == '__main__':
    pass