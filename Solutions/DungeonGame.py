class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        rows = len(dungeon)
        columns = len(dungeon[0])
        ret = [(0,0)] * columns
        if dungeon[rows-1][columns-1] > 0:
            ret[columns-1] = ((1, dungeon[rows-1][columns-1] + 1))
        else:
            ret[columns-1] = ((1 - dungeon[rows-1][columns-1]), 1)
        for i in range(columns-2, -1, -1):
            minItem = self.getMinItem(ret[i+1], dungeon[0][i])
            ret[i] = minItem
        
        # for i in range(rows-2,-1,-1):
        #     ret[columns-1] += dungeon[i][columns-1]
        #     for j in range(columns-2, -1, -1):



    def calculateMinimumHPMyWrongAnswer(self, dungeon):
        ret = []
        if dungeon[0][0] > 0:
            ret.append((1, dungeon[0][0] + 1))
        else:
            minHp = 1 - dungeon[0][0]
            ret.append((minHp, 1))
        for i in range(1, len(dungeon[0])):
            minItem = self.getMinItem(ret[i-1], dungeon[0][i])
            ret.append(minItem)
        
        for i in range(1, len(dungeon)):
            ret[0] = self.getMinItem(ret[0], dungeon[i][0])
            for j in range(1, len(dungeon[i])):
                path1 = self.getMinItem(ret[j], dungeon[i][j])
                path2 = self.getMinItem(ret[j-1], dungeon[i][j])
                ret[j] = self.compareItem(path1, path2)
        return ret[-1][0]
    
    def getMinItem(self, item, gridVal):
        if item[1] + gridVal > 0:
            return (item[0], item[1] +gridVal)
        else:
            extraHp = 1 - (item[1] + gridVal)
            return (item[0]+extraHp, 1)

    def compareItem(self, item1, item2):
        if item1[0] > item2[0]:
            return item2
        elif item1[0] < item2[0]:
            return item1
        elif item1[1] > item2[1]:
            return item1
        else:
            return item2


if __name__ == "__main__":
    print(Solution().calculateMinimumHP([[1,-3,3],[0,-2,0],[-3,-3,-3]]))