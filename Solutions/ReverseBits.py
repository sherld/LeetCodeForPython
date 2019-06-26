class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret = 0
        for _ in range(32):
            val = n & 1
            ret = (ret << 1) + val
            n = n >> 1
        return ret

if __name__ == "__main__":
    Solution().reverseBits(43261596)