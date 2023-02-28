class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self, prixHT):
        self.TVA = (self.prixHT * taux) / 100
        return self.TVA
        return self.prixHT
    
taux = 20
prix = Produit("banane", 2, 20 )
print(prix.calculerPrixTTC(24))