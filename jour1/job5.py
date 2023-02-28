class Point:
    def __init__(self, x, y):
        self.horizontal = x
        self.vertical = y

    def AfficherLesPoints(self):
        print (self.horizontal, self.vertical)
    
    def AfficherX(self):
        print(self.horizontal)

    def AfficherY(self):
        print(self.vertical)

    def ChangerX(self, change):
        self.horizontal = change + 1
        print(self.horizontal)

    def ChangerY(self, change):
        self.vertical = change + 1
        print(self.vertical)

coordonnee = Point(5, 7)
coordonnee.AfficherLesPoints()
coordonnee.AfficherX()
coordonnee.AfficherY()
coordonnee.ChangerX(6)
coordonnee.ChangerY(4)

