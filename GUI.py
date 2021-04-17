import tkinter
from tkinter import *
from board import board
class Checkerboard():
    curColor = "White"
    def __init__(self, checkers):
        top = tkinter.Tk()
        checkerboard = Canvas(top, width=700, height= 700)
        color = "red"
        x1 = 100
        x2 = 164
        y1 = 100
        y2 = 164
        for i in range(8):
            for j in range(8):
                checkerboard.create_rectangle(x1, y1, x2, y2, fill = color)
                if checkers.board[i][j] != None:
                    checkerboard.create_oval(x1, y1, x2, y2, fill = checkers.board[i][j].color)
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
        colorLabel = tkinter.Label(text="White's Turn")
        l1 = tkinter.Label(text="Initial x position")
        l2 = tkinter.Label(text="Initial Y position")
        l3 = tkinter.Label(text="Ending X position")
        l4 = tkinter.Label(text="Ending Y position")
        startX = tkinter.Entry()
        startY = tkinter.Entry()
        endX = tkinter.Entry()
        endY = tkinter.Entry()
        
        def moveUnit():
            try:
                curX = int(startX.get())
                curY = int(startY.get())
                x = int(endX.get())
                y = int(endY.get())
            except ValueError:
                print("Sorry, not an acceptable input")
                errorPopup()
                return 
            if checkers.placePiece(curX, curY, x, y, self.curColor):
                #Swap pieces
                temp = checkers.board[curX][curY] 
                checkers.board[curX][curY] = checkers.board[x][y]
                checkers.board[x][y] = temp
                #Update Board

                #Check if win conditions
                if checkers.win():
                    winPopup()
                #Change Turn
                if self.curColor == 'White':
                    self.curColor = 'Black'
                else:
                    self.curColor = 'White'
            else:
                errorPopup()
                print("Sorry, not an acceptable input")
            
        def errorPopup():
            errormessage = tkinter.Tk()
            errormessage.wm_title("Error")
            errorLabel = tkinter.Label(errormessage, text="Sorry, not an acceptable input")
            errorButton = tkinter.Button(errormessage, text="Okay", command = errormessage.destroy)
            errorLabel.pack()
            errorButton.pack()
            errormessage.mainloop()

        def winPopup():
            winMessage = tkinter.TK()
            winMessage.wm_title("Congratulations!")
            winLabel = tkinter.Label(winMessage, text="You won!")
            winButton = tkinter.Button(winMessage, text="Okay", command = winMessage.destroy)
            winLabel.pack()
            winButton.pack()
            winMessage.mainloop()

        button = tkinter.Button(text ="Click me.", command = moveUnit)
        colorLabel.pack()
        l1.pack()
        startX.pack()
        l2.pack()
        startY.pack()
        l3.pack()
        endX.pack()
        l4.pack()
        endY.pack()
        button.pack()
        checkerboard.pack()
        top.mainloop()