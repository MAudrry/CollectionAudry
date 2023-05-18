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