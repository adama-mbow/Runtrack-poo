class Rectangle:
    #constructuer
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
#assensseur
    def get_longueur(self):
        return self.__longueur
 #mutateur permet de modifier la valeur des attributs  
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur

rectangle = Rectangle(10, 5)
print("la longueur du rectangle est =", rectangle.get_longueur(), "et la largeur du rectangle est = ",  rectangle.get_largeur())
rectangle.set_longueur(6)
rectangle.set_largeur(10)
print("la longueur du rectangle est =", rectangle.get_longueur(), "et la largeur du rectangle est = ",  rectangle.get_largeur())