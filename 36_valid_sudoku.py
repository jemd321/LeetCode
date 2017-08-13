class ValidSudoku:
    def isValidSudoku(self, board):
        rows = board
        columns = ["".join(row[i] for row in board) for i in range(9)]
        squares = ["".join(rows[i:i+3][j][k:k+3] for j in range(3)) for k in range(0, 9, 3) for i in range(0, 9, 3)]

        for group in (rows, columns, squares):
            if not self.validate(group):
                return False
        return True

    def validate(self, group):
        is_valid = True
        for line in group:
            if len(line) != 9:
                is_valid = False
            for i in range(9):
                if line.count(str(i)) > 1:
                    is_valid = False
        return is_valid


test = ValidSudoku()
print(test.isValidSudoku(["53..7....",
                        "6..195...",
                        ".98....6.",
                        "8...6...3",
                        "4..8.3..1",
                        "7...2...6",
                        ".6....28.",
                        "...419..5",
                        "....8..79"]))
print(test.isValidSudoku(["555.7....",
                        "6..195...",
                        ".98....6.",
                        "8...6...3",
                        "4..8.3..1",
                        "7...2...6",
                        ".6....28.",
                        "...419..5",
                        "....8..79"]))