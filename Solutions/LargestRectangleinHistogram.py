class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxVal = 0
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                index = stack.pop()
                curArea = i*heights[index] if not stack else (i-stack[-1]-1)*heights[index]
                maxVal = max(maxVal, curArea)
            stack.append(i)
        while stack:
            index = stack.pop()
            curArea = len(heights) * heights[index] if not stack else (len(heights)-stack[-1]-1)*heights[index]
            maxVal = max(maxVal, curArea)
        return maxVal

if __name__ == "__main__":
    Solution().largestRectangleArea([2,1,5,6,2,3])