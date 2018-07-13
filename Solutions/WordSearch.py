class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        flag = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(board, word, list(flag), i, j, 0):
                        return True
        return False
    
    def dfs(self, board, word, flag, x, y, p):
        if p == len(word):
            return True
        if x < 0 or x >= len(board):
            return False
        if y < 0 or y >= len(board[0]):
            return False
        if flag[x][y]:
            return False
        if board[x][y] != word[p]:
            return False
        flag[x][y] = True
        ret = (self.dfs(board, word, flag, x-1, y, p+1) or self.dfs(board, word, flag, x+1, y, p+1)
                or self.dfs(board, word, flag, x, y-1, p+1) or self.dfs(board, word, flag, x, y+1, p+1))
        flag[x][y] = False
        return ret

    def existMine(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        flag = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfsMine(board, word, list(flag), i, j, 1):
                        return True
        return False
        
    def dfsMine(self, board, word, flag, x, y, p):
        if p == len(word):
            return True
        flag[x][y] = True
        if x > 0:
            if not flag[x-1][y] and board[x-1][y] == word[p]:
                flag[x-1][y] = True
                ret = self.dfsMine(board, word, flag, x-1, y, p+1)
                if ret:
                    return True
                flag[x-1][y] = False
        if x < len(board) - 1:
            if not flag[x+1][y] and board[x+1][y] == word[p]:
                flag[x+1][y] = True
                ret = self.dfsMine(board, word, flag, x+1, y, p+1)
                if ret:
                    return True
                flag[x+1][y] = False
        if y > 0:
            if not flag[x][y-1] and board[x][y-1] == word[p]:
                flag[x][y-1] = True
                ret = self.dfsMine(board, word, flag, x, y-1, p+1)
                if ret:
                    return True
                flag[x][y-1] = False
        if y < len(board[0])-1:
            if not flag[x][y+1] and board[x][y+1] == word[p]:
                flag[x][y+1] = True
                ret = self.dfsMine(board, word, flag, x, y+1, p+1)
                if ret:
                    return True
                flag[x][y+1] = False
        flag[x][y] = False
        return False

if __name__ == "__main__":
    Solution().exist([["a","a"]], "aaa")