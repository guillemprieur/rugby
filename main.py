import data
import www
if input("Quel programme voulez-vous utiliser ?) (1 ou 2) : ")=="1":
    import prog1
    liste_demandes=prog1.init()
    liste_dico=[]
    for journee in range(1,liste_demandes[2]+1):
        if not data.verif(str(liste_demandes[0])+str(liste_demandes[1])+str(journee)):
            www.download("https://"+liste_demandes[0]+".lnr.fr/classement/"+liste_demandes[1]+"/j"+str(journee),"data.html")
            data.creer(str(liste_demandes[0])+str(liste_demandes[1])+str(journee),www.extraire("data.html"))
            data.suppr_fichier("data.html")
        liste_dico.append(data.lire(str(liste_demandes[0])+str(liste_demandes[1])+str(journee)))
    
    prog1.exportation(data.clefs(liste_dico[len(liste_dico)-1]),liste_dico,liste_demandes)
else:
    import prog2
    import graphique
    if input("Voulez-vous utiliser ou supprimer un mode déjà sauvegardé ? (1=oui) : ")=="1":
        liste_equipes_etudiees=prog2.init2()
    else:
        liste_equipes_etudiees=prog2.init()
    equipes_etudiees={}
    for i in liste_equipes_etudiees:
        equipes_etudiees[i]=[40,40,40,40,40,40,40,40,40,40]
    division=["top14","prod2"]
    journee=[26,30]
    for i in range(2):
        liste_dico=[]
        for saison in graphique.saisons:
            if not data.verif(division[i]+saison+str(journee[i])):
                www.download("https://"+division[i]+".lnr.fr/classement/"+saison+"/j"+str(journee[i]),"data.html")
                data.creer(division[i]+str(saison)+str(journee[i]),www.extraire("data.html"))
                data.suppr_fichier("data.html")
            liste_dico.append(data.lire(division[i]+saison+str(journee[i])))    
        for j in range(10):
            saison=liste_dico[j]
            k=1
            for equipe in saison.keys():
                if equipe in equipes_etudiees.keys():
                    if division[i]=="top14":
                        equipes_etudiees[equipe][j]=k
                    else:
                        equipes_etudiees[equipe][j]=k+14
                k=k+1
    prog2.exportation(equipes_etudiees)