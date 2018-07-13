class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        length = len(board)
        container = set()

        # validation check for row
        for i in range(length):
            container.clear()
            for j in range(length):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in container:
                    container.add(board[i][j])
                else:
                    return False

        # validation check for column
        for i in range(length):
            container.clear()
            for j in range(length):
                if board[j][i] == '.':
                    continue
                if board[j][i] not in container:
                    container.add(board[j][i])
                else:
                    return False

        # validation check for block
        for i in range(0, length, 3):
            for j in range(0, length, 3):
                container.clear()
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y] == '.':
                            continue
                        if board[i+x][j+y] not in container:
                            container.add(board[i+x][j+y])
                        else:
                            return False
        return True