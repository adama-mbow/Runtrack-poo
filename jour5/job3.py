def retourner(mots):
    if len(mots) in [0,1]:
        return mots
    else:
        return mots[-1] + retourner(mots[:-1])
    
print(retourner("abcd"))