def transfo_division(var):
    if var=="1":
        return "top14"
    elif var=="2":
        return "prod2"

def init():
    division=transfo_division(input("Quelle est la division etudiee ? (1 ou 2) : "))
    saison=input("Quelle est la saison etudiee ? (attention au format : 20XX-20XX) : ")
    journee=int(input("Quelle est la derniere journee a prendre en compte ? : "))
    return [division,saison,journee]

def exportation(equipes,dictionnaires,data_utilisateur):
    import graphique
    from data import verif_dossier
    import matplotlib.pyplot as plt
    for i in range(len(equipes)):
        liste_points=[]
        for j in dictionnaires:
            liste_points.append(j[equipes[i]])
        plt.plot(range(1,data_utilisateur[2]+1),liste_points,color=graphique.couleurs[i],label=equipes[i])
    plt.title("Evolution des points des equipes du "+data_utilisateur[0]+" (saison "+data_utilisateur[1]+")")
    plt.legend(fontsize="7")
    verif_dossier("exportations")
    plt.savefig("exportations/"+data_utilisateur[0]+data_utilisateur[1]+".svg", format='svg', dpi=1200)
    plt.show()