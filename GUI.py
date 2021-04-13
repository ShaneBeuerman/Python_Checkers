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
        checkerboard.place(relx=0.5, rely=0.5, anchor=CENTER)
        checkerboard.pack()
        top.mainloop()