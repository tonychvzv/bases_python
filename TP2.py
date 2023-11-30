#réaliser une fonction qui affiche le nb de voyelles dans une chaine de caractère

vowels = "aeiouyAEIOUY"

def nbVow(chaine):
    #compteur pour faire plus propre
    compteur = 0
    for letter in chaine: 
        if letter in vowels: compteur +=1
    return compteur

print(nbVow("Bonjour TOI !"))