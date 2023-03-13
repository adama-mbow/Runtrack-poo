class Livre:
    def __init__(self, titre, auteur, nombre_de_page, disponible = True):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_page = nombre_de_page
        self.__disponible = disponible

    #assensseur
    def get_titre(self):
        return self.__titre
    #mutateur permet de modifier la valeur des attributs  
    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, auteur):
        self.__auteur = auteur

    
    def get_nombre_de_page(self):
        if self.__nombre_de_page % 2 == 0:
            self.__nombre_de_page +=1
            return self.__nombre_de_page
        else:
            return "Erreur le numero de la page doit etre multiple de 2 pour aller à la page suivante"
    
    def set_nombre_de_page(self, nombre_de_page):
        self.__nombre_de_page = nombre_de_page
        #for i in int(nombre_de_page):
        return nombre_de_page 
            
    def vérification(self): 
        if self.__disponible == True:
            return True
        else:
            return False  
            
livre = Livre("une si longue lettre", "Mariama Ba", 200)
print("le livre est intitulé ", livre.get_titre(), "il est ecrit par ", livre.get_auteur(), "et il contient ", livre.get_nombre_de_page(), "pages")
livre.set_titre("une vie de boy")
livre.set_auteur("Birago Diop")
livre.set_nombre_de_page(38)
livre.__disponible(True)
print("le livre est intitulé ", livre.get_titre(), "il est ecrit par ", livre.get_auteur(), "et je suis à la page ", livre.get_nombre_de_page(),)