class checker():
    def __init__(self, color, status, x, y):
        self.color = color
        self.status = status
        self.x = x
        self.y = y
    def kingMe(self):
        self.status = "King"
    def move(self, row, col):
        if self.status == "King":
            if (row == self.x+1 or row == self.x-1) and (col == self.y+1 or col == self.y-1):
                self.x = row
                self.y = col
                return True
            print("Can't move that way")
            return False

        if self.color == "Grey":
            if col == self.y+1 and (row == self.x+1 or row == self.x-1):
                if col == 7:
                    self.kingMe()
                self.x = row
                self.y = col
                return True
            print(col, row)
            print(self.x, self.y)
            print("Can't move that way")
            return False

        elif self.color == "White":
            if col == self.y-1 and (row == self.x+1 or row == self.x-1):
                if col == 0:
                    self.kingMe()
                self.x = row
                self.y = col
                return True
            print(col, row)
            print(self.x, self.y)
            print("Can't move that way")
            return False
