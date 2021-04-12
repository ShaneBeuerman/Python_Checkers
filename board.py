from checker import checker

class board():
    board = [[None]*8 for _ in range(8)]
    def __init__(self):

        
        self.board[0][1] = checker("Black", "Man", 0, 1)
        self.board[0][3] = checker("Black", "Man", 0, 3)
        self.board[0][5] = checker("Black", "Man", 0, 5)
        self.board[0][7] = checker("Black", "Man", 0, 7)

        self.board[1][0] = checker("Black", "Man", 1, 0)
        self.board[1][2] = checker("Black", "Man", 1, 2)
        self.board[1][4] = checker("Black", "Man", 1, 4)
        self.board[1][6] = checker("Black", "Man", 1, 6)

        self.board[2][1] = checker("Black", "Man", 2, 1)
        self.board[2][3] = checker("Black", "Man", 2, 3)
        self.board[2][5] = checker("Black", "Man", 2, 5)
        self.board[2][7] = checker("Black", "Man", 2, 7)

        self.board[5][0] = checker("White", "Man", 5, 0)
        self.board[5][2] = checker("White", "Man", 5, 2)
        self.board[5][4] = checker("White", "Man", 5, 4)
        self.board[5][6] = checker("White", "Man", 5, 6)
        
        self.board[6][1] = checker("White", "Man", 6, 1)
        self.board[6][3] = checker("White", "Man", 6, 3)
        self.board[6][5] = checker("White", "Man", 6, 5)
        self.board[6][7] = checker("White", "Man", 6, 7)

        self.board[7][0] = checker("White", "Man", 7, 0)
        self.board[7][2] = checker("White", "Man", 7, 2)
        self.board[7][4] = checker("White", "Man", 7, 4)
        self.board[7][6] = checker("White", "Man", 7, 6)

        
    def displayBoard(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == None:
                    print("_", end=" ")
                else:
                    print(self.board[i][j].color[0], end=" ")
            print()

    def placePiece(self, unit, x, y):
        if x > 7 or y > 7 or x < 0 or y < 0:
            print("Can't move that way.")
            return
        if unit.move(x, y):
            self.board[x][y] = unit
        else:
            print("Can't move that way")

    def win(self):
        #Set win condition
        print("incomplete")