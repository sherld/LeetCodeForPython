class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        rowLen = len(matrix)
        firstColumn = []
        for i in range(rowLen):
            firstColumn.append(matrix[i][0])
        x = self.search(firstColumn, target)
        y = self.search(matrix[x], target)
        return matrix[x][y] == target

    
    def search(self, array, target):
        length = len(array)
        lo = 0
        hi = len(array) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if array[mid] < target:
                lo = mid + 1
            elif array[mid] > target:
                hi = mid - 1
            else:
                return mid
        return hi