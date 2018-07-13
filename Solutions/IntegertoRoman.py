class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return m[num//1000] + c[(num%1000)//100] + x[(num%100)//10] + i[num%10]

    def intToRoman1(self, num):
        value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        letter = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        s = ''
        for idx, val in enumerate(value):
            while num >= val:
                num -= val
                s += letter[idx]
        return s

if __name__ == '__main__':
    print(Solution().intToRoman1(123))