# créer un programme sous forme de terminal permettant de
# calculer la surface et le volume 
# le programme devra afficher la liste des commandes sur demande
# et intégrer une commande pour quitter le programme

# aide, surface, volume, quitter et des exceptions d'erreur

dict0 = {"aide" : "affiche les commandes du programme", 
        "surface" : "calculer la surface en m2",
        "volume" : "calculer le volume en m3",
        "quitter" : "quitter le programme"}
# pas d'input - c'est un possible cul-de-sac    

print("Tapez aide pour afficher les commandes")

#commande "com>" = saisissez votre commande
while True:
    com = input("com>")

    if com=="aide":
        print("Liste des commandes du programme")
        print("--------------------------------")
        for k,v in dict0.items():
            print(k, ":", v)

# on aurait pu aussi faire un print avec la liste du dict0 mais
# cela aurait été moins efficace en cas de modifications

    elif com=="surface":
         long = input("Longueur ?")
         larg = input("Largeur ?")
         try:
             print(f"la surface est de {float(long)*float(larg)}m2")
         except:
             print("une erreur s'est produite")
             continue
    elif com=="volume":
         long = input("Longueur ?")
         larg = input("Largeur ?")
         haut = input("hauteur ?")
         try:
             print(f"le volume est de {float(long)*float(larg)*float(haut)}m3")
         except:
             print("une erreur s'est produite")
             continue
    elif com=="quitter": break
