class Solution:

    def isValidSudoku(self, board: list[list[str]]) -> bool:

        # check rows

        for row in board:
            val = list(filter(lambda x: x.isnumeric(), row))
            if len(val) != len(set(val)):
                return False

        # columns
        for j in range(9):
            col = {}
            for i in range(9):
                if not board[i][j].isnumeric():
                    pass
                elif col.get(j) is None:
                    col[j] = [board[i][j]]
                elif board[i][j] in col[j]:
                    return False
                else:
                    col[j].append(board[i][j])

        box = {}
        for i in range(9):
            for j in range(9):
                wb = self.whichBox(i, j)

                if not board[i][j].isnumeric():
                    pass
                elif box.get(wb) is None:
                    box[wb] = [board[i][j]]

                elif board[i][j] in box[wb]:
                    return False
                else:
                    box[wb].append(board[i][j])

        return True

    def whichBox(self, x, y) -> int:
        return int(y/3) + 1 + (int(x/3)*3)


if __name__ == "__main__":
    boardT = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                           ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    boardF = [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".",
                                                                                                                                                                                                           "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
sol = Solution()
solb = Solution()
a = sol.isValidSudoku(boardT)
b = solb.isValidSudoku(boardF)
print(a)
print(b)
