class Personne:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    def Sepresenter(self):
        print("je m'appelle " + self.prenom, self.nom)

Personne1 = Personne("jean", "smith")
Personne1.Sepresenter()