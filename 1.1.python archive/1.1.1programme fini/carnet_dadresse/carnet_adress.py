'''
programme name

projet de carnet d'adresse. but:creation d'une classe et des objet

13/07/2021
by: desnyt628
##################################################################
####_#####################_#######################_###############
###| |############_######| |#####################| |##############
###| |__##_ ##_##(_)###__| |#___##___ _#__##_###_| |_## /!_/!   _#
###| '_ \| | | |######/ _` |/ _ \/ __| '_ \| |#| | __|#(=0-0=) //#
###| |_) | |_| |##_##| (_| |  __/\__ \ |#| | |_| | |_## !  _ \// #
###|_.__/#\__, |#(_)##\__,_|\___||___/_|#|_|\__, |\__|# UUC___)  #
###########__/ |#############################__/ |################
##########|___/############628##############|___/#####it's a cat!#
##################################################################
''' 
###import
import pickle
import os.path
import time
###constante
test=('sa fonctionne')
nomfichier_save="popo.pickle"
exit0="voulez vous vraiment quitter(y/n)?"
instruction="""
*********************************************

       Application Carnet d'Adresses
       
              desnyt628
              
*********************************************
Tapez une des quatre touches suivantes :
A pour Ajouter une personne
L pour la Liste des fiches du carnet
I pour revoir ces Instructions
Q pour Quitter
S pour sauvgarder
"""
###class
class CarnetAdr(object):
    """conteneur de fichier"""
    def __init__(self):
        "liste contenant toute les info selon les personne"
        self.gens=[]
    def ajouter_fiche(self,new_file):
        """ajouter une fichi a self.gens
        new_file=contact1"""
        self.gens.append(new_file)
    def Save(self):
        with open(nomfichier_save,'wb') as allo:
            pickle.dump(self,allo)   
    def __repr__(self):
        coucou=str(self.gens)
        return coucou
class FicheAdr(object):
    """on fait apelle a la classe on lui donne les information et il cree un tuple"""
    def __init__(self,prenom=None,nomfami=None,datenais=None,courriel=None):
        """mes en place les 4 atribut. 
        datenais est sous format JJ/MM/AAAA"""
        self.prenom = prenom
        self.nomfami=nomfami
        self.datenais=datenais
        self.courriel=courriel
    def __repr__(self):
        patron= "FichAdr(\nprenom=%s\n"+\
        "nomfami=%s\n"+\
        "datenaissance=%s\n"+\
        "courriel=%s\n)"
        return patron%(self.prenom,self.nomfami,self.datenais,self.courriel)
class kontroleur(object):
    """controle lensemble (regarde si il y a deja un fichier a charger
    ou si y doit en cree un """
    def __init__(self):
        ''''cree un fichier pour stocker les adresse si il en a pas deja un'''
        self.carnet_adr=self.charger()
        if self.carnet_adr is None:
            self.carnet_adr=CarnetAdr()
        self.menu()
    def charger(self):
        if os.path.exists(nomfichier_save):
            with open(nomfichier_save,'rb') as hey:
                return pickle.load(hey)
        else:
            return None
    def menu(self):
        print(instruction)
        while True:
            cmd=str(input(">"))
            if cmd=='a':
                self.ajouter_fiche()
            elif cmd=='q':
                if confexit():
                    print("sauvrgade en cour...")
                    self.carnet_adr.Save()
                    print("sauvgarde terminer")
                    time.sleep(3)
                    break
                else:
                    pass
            elif cmd=='l' :
                self.lister_fiche()
            elif cmd=='s':
                self.carnet_adr.Save()
            elif cmd=='i':
                print(instruction)
            else:
                model="> %s n'est pas une commande faite 'i' pour voir les commandes disponibles"
                print(model%cmd)

    def ajouter_fiche(self):
        '''demande les variable de la nouvelle fiche'''
        print("\najout d'une fiche dans le carnet.")
        print("'#q' pour quitter en cour de creation.")
        print("description de la personne.\n")
        prenom=input("prenom:")
        if prenom=='#q':
            return
        nomfamil=input("nom de famille:")
        if nomfamil=='#q':
            return
        datnais=input("date de naissance(jj/MM/AAAA):")
        if datnais=='#q':
            return
        couriel=input("couriel:")
        if couriel=='#q':
            return
        nfiche=FicheAdr(prenom,nomfamil,datnais,couriel)
        self.carnet_adr.ajouter_fiche(nfiche)
    def lister_fiche(self):
        '''afficher une liste des contacte enregistrer '''
        patronliste="%s %s\n   date de naissance: %s\n   couriel: %s\n\n"
        for numero, e in enumerate(self.carnet_adr.gens):
            contact=(e.prenom,e.nomfami,e.datenais,e.courriel)
            fiche=patronliste%contact
            print(" %s.%s "%(numero+1,fiche))
###fonction
def confexit():
    """confirmation avant de quitter"""
    confirmation=input("est tu sur de vouloir quitter? y/n \n>")
    if confirmation=="n":
        return False
    elif confirmation=='y':
        return True
    else:
        return False
###main
if __name__=="__main__":
    k=kontroleur()
#EOF