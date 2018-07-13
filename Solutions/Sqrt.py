class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x == 1:
            return 1
        lo = 1
        hi = x // 2
        while lo <= hi:
            mid = (lo + hi) // 2
            product = mid * mid
            if product == x:
                return mid
            elif product < x:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo - 1

if __name__ == "__main__":
    print(Solution().mySqrt(1))