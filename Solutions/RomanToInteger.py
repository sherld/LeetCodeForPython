class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter = ["M","D","C","L","X","V","I"]
        value = [1000,500,100,50,10,5,1]
        relation = dict(zip(letter, value))
        sum = 0
        lastVal = 0
        for idx, char in enumerate(s):
            if idx == 0 or relation[char] <= lastVal:
                sum += relation[char]
                lastVal = relation[char]
            else:
                sum += relation[char]
                sum -= 2 * lastVal
                lastVal = relation[char]
        return sum
            

        
if __name__ == '__main__':
    print(Solution().romanToInt("MDCCCXCIX"))