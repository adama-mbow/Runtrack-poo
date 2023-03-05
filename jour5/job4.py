#Écrire une fonction récursive permettant de retourner le plus grand chiffre d’une liste.

def chiffre(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        return max(liste[0], chiffre(liste[1:]))

liste = [54,9,2,14,35,10,36,8,45,68]   
print(chiffre(liste))

