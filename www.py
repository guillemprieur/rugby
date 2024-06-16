def download(lien,destination):
    from requests import get
    fichierHTML=get(lien)
    open(destination,"w").write(fichierHTML.text)

def extraire(source):
    from bs4 import BeautifulSoup
    classement = BeautifulSoup(open(source,"r"),"html.parser").find_all("div",class_="table-line table-line--ranking-full table-line--ranking-scrollable")
    dico={}
    for equipe in classement:
        nom=equipe.find("div",class_="table-line__cell-wrapper table-line__cell-wrapper--full table-line__cell-wrapper--club-name").find("a").string
        points = int(equipe.find("div",class_="table-line__cell--small").string)
        dico[nom[1:]]=points
    return dico

def equipes():
    from data import verif,lire
    if not verif("equipes_prod2"):
        from data import creer,suppr_fichier
        download("https://prod2.lnr.fr/classement/2023-2024/j30","data.html")
        creer("equipes_prod2",extraire("data.html"))
        suppr_fichier("data.html")
    if not verif("equipes_top14"):
        from data import creer,suppr_fichier
        download("https://top14.lnr.fr/classement/2023-2024/j26","data.html")
        creer("equipes_top14",extraire("data.html"))
        suppr_fichier("data.html")
    return [lire("equipes_top14"),lire("equipes_prod2")]