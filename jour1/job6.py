class Animal:
    def __init__(self, prenom):
        self.age = 0
        self.prenom = prenom
        print("l'age de l'animal ", self.age, "ans")

    def Vieillir(self):
        vieillir = self.age + 1
        print("l'age de l'animale ", vieillir, "ans.")

    def Nommer(self):
        print("l'animal se nomme ", self.prenom)

animal = Animal("ladoume")
animal.Vieillir()
animal.Nommer()