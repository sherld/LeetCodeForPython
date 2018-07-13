class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'

        len1 = len(num1)
        len2 = len(num2)

        ret = ''
        remain = 0

        for i in range(len1 + len2 - 1):
            sum = 0
            sum += remain
            for j in range(len2 - 1, -1, -1):
                k = len1 + len2 - 2 - i - j
                if k >= 0 and k < len1:
                    sum += int(num1[k]) * int(num2[j])
            remain = sum // 10
            ret += str(sum % 10)
        if remain > 0:
            ret += str(remain)
        return ret[::-1]

if __name__ == '__main__':
    print(Solution().multiply('6', '5'))
