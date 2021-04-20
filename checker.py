class checker():
    def __init__(self, color, status, x, y):
        self.color = color
        self.status = status
        self.x = x
        self.y = y
    def kingMe(self):
        self.status = "King"
    def move(self, col, row):
        if self.status == "King":
            if (row == self.x+1 or row == self.x-1) and (col == self.y+1 or col == self.y-1):
                return True
            print("Can't move that way")
            return False

        if self.color == "Grey":
            if row == self.x+1 and (col == self.y+1 or col == self.y-1):
                return True
            print(col, row)
            print(self.x, self.y)
            print("Can't move that way")
            return False

        elif self.color == "White":
            if row == self.x-1 and (col == self.y+1 or col == self.y-1):
                return True
            print(col, row)
            print(self.x, self.y)
            print("Can't move that way")
            return False
