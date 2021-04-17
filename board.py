from checker import checker

class board():
    board = [[None]*8 for _ in range(8)]
    def __init__(self):
        
        self.board[0][1] = checker("Grey", "Man", 0, 1)
        self.board[0][3] = checker("Grey", "Man", 0, 3)
        self.board[0][5] = checker("Grey", "Man", 0, 5)
        self.board[0][7] = checker("Grey", "Man", 0, 7)

        self.board[1][0] = checker("Grey", "Man", 1, 0)
        self.board[1][2] = checker("Grey", "Man", 1, 2)
        self.board[1][4] = checker("Grey", "Man", 1, 4)
        self.board[1][6] = checker("Grey", "Man", 1, 6)

        self.board[2][1] = checker("Grey", "Man", 2, 1)
        self.board[2][3] = checker("Grey", "Man", 2, 3)
        self.board[2][5] = checker("Grey", "Man", 2, 5)
        self.board[2][7] = checker("Grey", "Man", 2, 7)

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

    def placePiece(self, initX, initY, desX, desY, color):
        if initX > 7 or initY > 7 or initX < 0 or initY < 0:
            print("Initial Position is incorrect")
            return False
        if desX > 7 or desY > 7 or desX < 0 or desY < 0:
            print("Destination is incorrect")
            return False
        if self.board[initX][initY] == None:
            print("No Piece there. Try Again.")
            return False
        if self.board[initX][initY].color != color:
            print("Can't move opponent's piece")
            return False
        if self.board[desX][desY] != None:
            print("Another piece sits there.")
            return False
        if self.board[initX][initY].move():
            return True
        print("Sorry, didn't work")
        return False

    def win(self):
        #Set win condition
        whiteCount = 0
        blackCount = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j].color == "Black":
                    blackCount = 1
                if self.board[i][j].color == "White":
                    whiteCount = 1
                if whiteCount == 1 and blackCount == 1:
                    return False
        if whiteCount == 0:
            print("White Loses")
            return True
        elif blackCount == 0:
            print("Black loses")
            return True
        return False