class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self):
        print( "le nouveau rayon est ", self.rayon,"cm")
        self.rayon +=1

    def afficherInfo(self):
        diametre = self.rayon * 2
        perimetre = diametre * 3.14
        print("on a un cercle de rayon ", self.rayon,"cm ", "avec un diametre de ", diametre,"cm " "et un perimetre de ", perimetre,"cm")

    def circonference(self):
        circonference = self.rayon * 2 * 3.14
        print("la circonference est egale à ", circonference,"cm")

    def air(self):
        air = (self.rayon**2) * 3.14
        print("l'air du cercle est de ", air)    

cercle1 = Cercle(4)
cercle2 = Cercle(7)
cercle1.changerRayon()
cercle1.afficherInfo()
cercle1.circonference()
cercle1.air()
cercle2.changerRayon()
cercle2.afficherInfo()
cercle2.circonference()
cercle2.air()