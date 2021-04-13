from board import board
from checker import checker
from GUI import Checkerboard

Checkerboard()
checkers = board()
#checkers.displayBoard()
testChecker = checker("Black", "Man", 0, 1)
testChecker.move(0,0)
turn = "W"
print("White moves first")
while True:
    x = input("Choose an x position.")
    y = input("Choose a y position")
    # Move Piece
    # Check win condition checkers.win()
    # Display board
    if turn == 'B':
        print("White's turn")
        turn = 'W'
    else:
        print("Black's turn")
        turn = 'B'
    if x == "Q":
        break
