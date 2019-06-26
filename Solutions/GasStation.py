class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        diff = [x-y for x, y in zip(gas, cost)]
        sum = 0
        start = 0
        total = 0
        for i in range(len(gas)):
            sum += diff[i]
            if sum < 0:
                start = i + 1
                total += sum
                sum = 0
        return -1 if sum + total < 0 else start

if __name__ == "__main__":
    Solution().canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2])