if __name__ == '__main__':
    # Q1.Création d'une liste
    voitures=["Vanguard","Mitsubishi","T.I","Probox","MacLaren","Mercedes","Allione","Rav 4","Porshe","Ferarri"]
    # Fin de la création de la liste

    # Q1.1 Affichage des éléments de la liste

    print("\nQ1.1 Affichage des elements de la liste")
    print("-------------------------------------------\n")
    for voiture in voitures:
        print(voiture)

    # Fin de l'affichage des éléments de la liste

    # Q1.2 Changer le contenu de l'élément numéro 5
    voitures[5]= "Citroen"
    # Q1.2 Fin du Changement de l'élément 5

    # Q1.3 Création d'une nouvelles liste en remplissant la précente
    Nouvelles_voitures = [v for v in voitures if 'a' in v]
    Nouvelles_voitures.extend(["Hilux","Porte","vitz","Sienta"])

    print("\nQ1.3 Affichage de la nouvelles liste cree en remplissant la precente qui a 'a' dans ses elements")
    print("---------------------------------------------------------------------------------------------------\n")
    for V in Nouvelles_voitures:
        print(V)
    # Fin de la création de la nouvelle liste

    #Q1.4 Ajouter un element a la fin de la liste
    voitures.append("Stechene")

    # Fin de l'ajout de l'élément


    #Q1.5 Ajouter un élément à l'index numéro 2 à la liste
    voitures.insert(2,"Spacio")

    # Fin de l'ajout de l'élément à l'index 2

    # Q1.6 supprimer l'element a l'index numero 3 de la liste
    del voitures[3]
    # FIN Q1.6  

    # Q1.7 supprimer l'element a l'index numero 2 de la liste
    del voitures[2]
    # FIN Q1.7   
       
    # Q1.8 Ordonner la liste
    print("\nQ1.8 Ordonner la liste")
    print("---------------------------------------------------------\n")
    voitures.sort()
    print("Affichage de la liste ordonnee:\n")
    for voiture in voitures:
        print(voiture)
 
    # FIN Q1.8   

     # Q1.9 Afficher  la liste au sens inverse
    print("\nQ1.9 Afficher  la liste au sens inverse")
    print("--------------------------------------------\n")
    voitures.reverse()
    print("Affichage de la liste au sens inverse:\n")
    for voiture in voitures:
        print(voiture)
 
    # FIN Q1.9  
    
     # Q1.10 Vider  la liste
    print("\nQ1.10 Vidage et Affichage de  la liste vide")
    print("--------------------------------------------\n")
    voitures.clear()
    print("voitures:",voitures)
 
    # FIN Q1.10 
        
       
     # Q1.11 Supprimer  la liste
    print("\nQ1.11 suppression de  la liste")
    print("--------------------------------------------\n")
    del voitures
    print("la liste voitures n'existe plus!!!!!!!!!\n\n")
 
    # FIN Q1.11

    # Q2 Créer une tuple de 10 éléments entiers
    Nombres = (1,3,6,3,4,3,4,8,5,3)
    # FIN Q2

    # Q2.1 Afficher le nombre de fois 3 apparait dans la tuple
    print("\nQ2.1 Afficher le nombre de fois 3 apparait dans la tuple")
    print("---------------------------------------------------\n")
    occurence = Nombres.count(3)
    print("Le nombre 3 apparait:",occurence,"fois")
    # FIN Q2.1

    # Q2.2 Afficher le contenu de l'element numero 5
    print("\nQ2.2 Afficher le contenu de l'element numero 5")
    print("---------------------------------------------------\n")
    contenu = Nombres[5]
    print("L'element 5 est:",contenu)
    # FIN Q2.2

    # Q2.3 Ordonner la tuple
    print("\nQ2.3 Ordonner la tuple")
    print("-----------------------------\n")
    NombresOrdonnes = sorted(Nombres)
    print("Tuple ordonnee:",NombresOrdonnes)
    # FIN Q2.3

    # Q2.4 Ajouter un element a la fin de la tuple
    print("\nQ2.4 Ajouter un element a la fin de la tuple")
    print("-----------------------------\n")
    Nombres = Nombres+(55,)
    print("t:",Nombres)
    # FIN Q2.4

    # Q2.5 Ajouter un element a l'index numero 3
    print("\nQ2.5 Ajouter un element a l'index numero 3")
    print("-----------------------------\n")
    Nombres = Nombres[:3]+(10,3,4, 3, 4, 8, 5, 3, 55)
    print("t:",Nombres)
    # FIN Q2.5

    # Q2.6 Afficher la nouvelle tuple
    print("\nQ2.6 Afficher la nouvelle tuple")
    print("-----------------------------\n")
    print("Nouvelle tuple:",Nombres)
    # FIN Q2.6
