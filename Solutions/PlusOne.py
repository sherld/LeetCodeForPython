class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        digits[len(digits) - 1] += 1
        for i in range(len(digits) - 1, -1, -1):
            sum = digits[i] + carry
            digits[i] = sum % 10
            carry = sum // 10
        if carry == 1:
            digits.insert(0, 1)
        return digits

if __name__ == "__main__":
    Solution().plusOne([1,2,3])
