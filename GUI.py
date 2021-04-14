import tkinter
from tkinter import *
from board import board

class Checkerboard():
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
        curColor = "White"
        colorLabel = tkinter.Label(text=curColor+"'s Turn")
        l1 = tkinter.Label(text="Initial x position")
        l2 = tkinter.Label(text="Initial Y position")
        l3 = tkinter.Label(text="Ending X position")
        l4 = tkinter.Label(text="Ending Y position")
        startX = tkinter.Entry()
        startY = tkinter.Entry()
        endX = tkinter.Entry()
        endY = tkinter.Entry()

        def displayInfo():
            try:
                curX = int(startX.get())
                curY = int(startY.get())
                x = int(endX.get())
                y = int(endY.get())
            except ValueError:
                print("Sorry, not an acceptable input")
                #popup error message
                return
            print("Current x:",curX)
            print("Current y:",curY)
            print("Ending X position:",x)
            print("Ending Y position:",y)
            

        button = tkinter.Button(text ="Click me.", command = displayInfo)
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