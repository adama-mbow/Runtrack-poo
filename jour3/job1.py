class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

class Personne(Ville):
    def __init__(self, nom, age,nombre_habitants):
            Ville.__init__(self, nom, age, nombre_habitants):          
            self.__nombre_habitants = nombre_habitants

    
              
    def ajouterPersonne(self, nombre_habitants):
        for i in  self.__nombre_habitants:
             self.__nombre_habitants +=1
             return self.__nombre_habitants            
    
    population = Ville.Personne("Paris", 1000000)
    print(population.ajouterPersonne)