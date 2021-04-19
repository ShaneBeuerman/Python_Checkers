import tkinter
from tkinter import *
from board import board
class Checkerboard():
    curColor = "White"
    top = tkinter.Tk()
    checkers = board()
    startX = tkinter.Entry()
    startY = tkinter.Entry()
    endX = tkinter.Entry()
    endY = tkinter.Entry()
    checkerboard = Canvas(top, width=700, height= 700)


    def __init__(self):
        self.updateBoard()
        colorLabel = tkinter.Label(text="White's Turn")
        l1 = tkinter.Label(text="Initial x position")
        l2 = tkinter.Label(text="Initial Y position")
        l3 = tkinter.Label(text="Ending X position")
        l4 = tkinter.Label(text="Ending Y position")           

        button = tkinter.Button(text ="Click me.", command = self.moveUnit)
        colorLabel.pack()
        l1.pack()
        self.startX.pack()
        l2.pack()
        self.startY.pack()
        l3.pack()
        self.endX.pack()
        l4.pack()
        self.endY.pack()
        button.pack()
        self.checkerboard.pack()
        self.top.mainloop()

    def updateBoard(self):
        color = "red"
        x1 = 100
        x2 = 164
        y1 = 100
        y2 = 164
        for i in range(8):
            for j in range(8):
                self.checkerboard.create_rectangle(x1, y1, x2, y2, fill = color)
                if self.checkers.board[i][j] != None:
                    self.checkerboard.create_oval(x1, y1, x2, y2, fill = self.checkers.board[i][j].color)
                x1 += 64
                x2 += 64
                if color == "red":
                    color = "black"
                else:
                    color = "red"
            y1 += 64
            y2 += 64
            x1 = 100
            x2 = 164
            if color == "red":
                color = "black"
            else:
                color = "red"
    
    def moveUnit(self):
        try:
            curX = int(self.startX.get())
            curY = int(self.startY.get())
            x = int(self.endX.get())
            y = int(self.endY.get())
        except ValueError:
            print("Sorry, not an acceptable input")
            self.errorPopup()
            return 
        if self.checkers.placePiece(curX, curY, x, y, self.curColor):
            #Swap pieces
            temp = self.checkers.board[curX][curY] 
            self.checkers.board[curX][curY] = self.checkers.board[x][y]
            self.checkers.board[x][y] = temp
            #Update Board
            self.updateBoard()
            self.checkers.displayBoard()
            #Check if win conditions
            if self.checkers.win():
                self.winPopup()
            #Change Turn
            if self.curColor == 'White':
                self.curColor = 'Grey'
            else:
                self.curColor = 'White'
        else:
            self.errorPopup()
            print("Sorry, not an acceptable input")

    def errorPopup(self):
        errormessage = tkinter.Tk()
        errormessage.wm_title("Error")
        errorLabel = tkinter.Label(errormessage, text="Sorry, not an acceptable input")
        errorButton = tkinter.Button(errormessage, text="Okay", command = errormessage.destroy)
        errorLabel.pack()
        errorButton.pack()
        errormessage.mainloop()

    def winPopup(self):
        winMessage = tkinter.Tk()
        winMessage.wm_title("Congratulations!")
        winLabel = tkinter.Label(winMessage, text="You won!")
        winButton = tkinter.Button(winMessage, text="Okay", command = winMessage.destroy)
        winLabel.pack()
        winButton.pack()
        winMessage.mainloop()