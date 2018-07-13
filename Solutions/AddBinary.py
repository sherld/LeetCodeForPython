class Solution:
    def addBinary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        ret = ""
        while i >= 0 or j >= 0:
            if i < 0:
                sum = int(b[j]) + carry
                ret += str(sum % 2)
                carry = sum // 2
                j -= 1
            elif j < 0:
                sum = int(a[i]) + carry
                ret += str(sum % 2)
                carry = sum // 2
                i -= 1
            else:
                sum = int(a[i]) + int(b[j]) + carry
                ret += str(sum % 2)
                carry = sum // 2
                i -= 1
                j -= 1
        if carry == 1:
            ret += "1"
        return ret[::-1]

    
    def addBinaryMine(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        reversedA = a[::-1]
        reversedB = b[::-1]
        lenA = len(a)
        lenB = len(b)
        minLen = min(lenA, lenB)
        carry = 0
        ret = ""

        for i in range(minLen):
            sum = int(reversedA[i]) + int(reversedB[i]) + carry
            ret += str(sum % 2)
            carry = sum // 2
        
        if lenA < lenB:
            for i in range(minLen, lenB):
                sum = int(reversedB[i]) + carry
                ret += str(sum % 2)
                carry = sum // 2
        else:
            for i in range(minLen, lenA):
                sum = int(reversedA[i]) + carry
                ret += str(sum % 2)
                carry = sum // 2
        
        if carry == 1:
            ret += "1"
        
        return ret[::-1]

if __name__ == "__main__":
    Solution().addBinary("111", "1")