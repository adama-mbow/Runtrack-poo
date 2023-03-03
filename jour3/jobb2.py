class CompteBancaire:
    def __init__(self, numero_de_compte, nom_prenom, solde, decouvert):
        self.__numero_de_compte = numero_de_compte
        self.__nom_prenom = nom_prenom
        self.__decouvert = decouvert
        self.__solde = solde

    def afficher(self):
        """self.numero_de_compte = self.numero_de_compte
        self.nom_prenom = self.nom_prenom
        self.solde = self.solde"""
        print ("Numero de compte: ", self.__numero_de_compte)
        print ("propriétère du compte: ", self.__nom_prenom)
        print ("solde: ", self.__solde,"euro") 

    def afficherSolde(self):
        self.__solde = self.__solde
        print(self.__solde, "euro")

    def versemment(self, somme):
        self.__solde = self.__solde + somme

    def retrait(self, montant_retire):
        self.___solde = self.__solde - montant_retire
        if self.__solde < montant_retire:
            print("Erreur: solde insuffisant! ")
        else:
            return self.__solde
        
    def agios(self):
        if self.__solde < 0:
            self.solde = self.solde * 95/100
            print(self.__solde, "euro")
        else:
            return self.__solde

    def virement(self, Beneficiaire, montant):
        self.__Beneficiaire = Beneficiaire
        if montant < self.__solde or self.__decouvert:
            self.___solde = self.__solde - montant
            self.agios()
            solde_Beneficiaire = self.__solde + montant
            print("Solde de ", self.__nom_prenom, "après virement est ", self.__solde)
            print("Solde de ", self.__Beneficiaire, "après virement est")

        else:
            print("Virement refusé : solde insuffisant")  
        
            


compte_1 = CompteBancaire(5412458744, " isacc mendez", 15000, True)
compte_2 = CompteBancaire(17651991, "Albert dupont", 14000, False)
compte_1.afficher()
compte_1.afficherSolde()
compte_1.retrait(300) 
compte_1.virement(compte_2, 2800 )

