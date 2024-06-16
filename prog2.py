def init():
    import www
    equipes=www.equipes()
    choix=[]
    print("Voici les club proposés :")
    for division in equipes:
        for club in division:
            if input("Souhaitez-vous ajouter "+club+' ? (Si oui répondez "y", sinon tapez entrer) : ')=="y":
                choix.append(club)
    if input("Souhaitez-vous enregistrer votre sélection ? (oui ou non) : ")=="oui":
        import data
        nomSauv=input("Donnez un nom pour la sauvegarde : ")
        data.verif_dossier("data")
        data.creer(nomSauv+"s", choix)
        data.append_pickle("init", nomSauv)
    return choix

def init2():
    import data
    data.verif_dossier("data")
    if data.verif("init"):
        for sauvegarde in data.lire("init"):
            supprouenr=input("Voulez-vous utiliser/supprimer "+sauvegarde+" ? (0= rien 1=utiliser 2=supprimer) : ")
            if supprouenr=="1":
                return data.lire(sauvegarde+"s")
            elif supprouenr=="2":
                if input("Etes vous sûr de vouloir supprimer cette sauvegarde ? (oui/non) : ")=="oui":
                    suppr_enr(sauvegarde)
                    print("Sauvegarde correctement supprimé !")
    print("Aucune sauvegarde choisie, veuillez en créer une...")
    return init()

def suppr_enr(nom):
    import data
    liste=data.lire("init")
    liste2=[]
    for mode_enr in liste:
        if not nom==mode_enr:
            liste2.append(mode_enr)
    data.creer("init",liste2)
    data.suppr(nom+"s")

def exportation(dictionnaires):
    import matplotlib.pyplot as plt
    import graphique
    fig,ax=plt.subplots()
    for i,j in dictionnaires.items():
        plt.plot(graphique.saisons,j,label=i) 
    plt.legend(fontsize="7")
    ax.set_ylim(30.5,0.5)
    plt.show()