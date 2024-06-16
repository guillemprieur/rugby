def verif_dossier(lien):
    from os import path, mkdir
    if not path.exists(lien):
        mkdir(lien)

def verif(nom):
    from os import path
    return path.isfile("data/"+nom+".pickle")

def creer(nom,donnee):
    from pickle import dump
    verif_dossier("data")
    fichier_donnee=open("data/"+nom+".pickle","wb")
    dump(donnee,fichier_donnee)
    fichier_donnee.close

def lire(nom):
    from pickle import load
    verif_dossier("data")
    if verif(nom):
        return load(open("data/"+nom+".pickle", "rb"))
    
def suppr(nom):
    from os import remove
    remove("data/"+nom+".pickle")

def suppr_fichier(source):
    from os import remove
    remove(source)

def clefs(dico):
    liste=[]
    for cle in dico.keys():
        liste.append(cle)
    return liste

def append_pickle(nom,donnee):
    if verif(nom):
        liste=lire(nom)
    else:
        liste=[]
    liste.append(donnee)
    creer(nom, liste)