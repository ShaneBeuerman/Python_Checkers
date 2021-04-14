from board import board
from checker import checker
from GUI import Checkerboard

checkers = board()
game = Checkerboard(checkers)
#checkers.displayBoard()
#testChecker = checker("Black", "Man", 0, 1)
#testChecker.move(0,0)
#turn = "W"
#print("White moves first")
#while True:
    #xStart = input("Choose your starting x position")
    #yStart = input("Choose your starting y position")
    #if int(xStart) > 8 or int(yStart) > 8 or int(xStart) < 0 or int(yStart) < 0:
        #print("Sorry but that input doesn't work")
        #continue
    #x = input("Choose an x position.")
    #y = input("Choose a y position")
    #if int(x) > 8 or int(y) > 8 or int(x) < 0 or int(y) < 0:
        #print("Sorry but that input doesn't work")
        #continue
    ## Move Piece
    ## Check win condition checkers.win()
    ## Display board
    #if turn == 'B':
        #print("White's turn")
        #turn = 'W'
    #else:
        #print("Black's turn")
        #turn = 'B'