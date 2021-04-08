class checker():
    def __init__(self, color, status, x, y):
        self.color = color
        self.status = status
        self.x = x
        self.y = y
    def kingMe(self):
        self.status = "King"
    def move(self, col, row):
        if col < 0 or col > 7 or row < 0 or row > 7:
            print("Can't move that way")
            return False

        if self.status == "King":
            if (row == self.y+1 or row == self.y-1) and (col == self.x+1 or col == self.x-1):
                return True
            print("Can't move that way")
            return False

        if self.color == "Black":
            if row == self.y+1 and (col == self.x+1 or col == self.x-1):
                return True
            print("Can't move that way")
            return False

        elif self.color == "White":
            if row == self.y-1 and (col == self.x+1 or col == self.x-1):
                return True
            print("Can't move that way")
            return False
