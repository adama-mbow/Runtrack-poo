class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def gauche(self):
        gauche = self.x - 1
        print("avancer à gauche de ", gauche, "position")
        
    def droite(self):
        droite = self.x + 1
        print("avancer à droite de ", droite, "position")

    def haut(self):
        haut = self.y + 1
        print("avancer vers le haut de ", haut, "position")

    def bas(self):
        bas = self.y - 1
        print("avancer vers le bas de  ", bas, "position")
position  = Personnage(5, 6)
position.gauche()
position.droite()
position.haut()
position.bas()