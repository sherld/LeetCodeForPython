class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        array = [i for i in range(1, n + 1)]
        count = 1
        step = n - 1
        ret = ""
        for i in range(1, n):
            count *= i
        k = k - 1
        while len(array) != 1:
            quotient = k // count
            k = k % count
            count = count // step
            step -= 1
            ret += str(array[quotient])
            del array[quotient]
        return ret + str(array[0])

if __name__ == "__main__":
    print(Solution().getPermutation(1,1))