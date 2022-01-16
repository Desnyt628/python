"""phrase en folie project make 
a sentence in french with ramdom word

10/02/2021 - 00/00/2021
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
"""
###import
import random
###constant
phrase_base= 'mon professeur programme un jeux formidable'
###variable
patron="%s %s %s %s"


###def
def phrase_h():
    """dss"""
    sujet=['mon professeur','ton pere','la madame','ta soeur','le chien','le chat','albert et leon','desnyt']
    verbe=['programme','joue a','lance','arrose','kick','tue','ecrit','nettoie','fabrique','vole']
    objet=['un jeux','un ordi','une ps5','un arbre',"l'avion",'un clavier','un easter egg']
    qualificatif=['formidable','magique','du future','pour manger','pour rien','car ses amusant',\
          'du demon','matinal','en rabais']
    sujet=random.choice(sujet) 
    verbe=random.choice(verbe)
    objet=random.choice(objet)
    qualificatif=random.choice(qualificatif)
    valformat=(sujet,verbe,objet,qualificatif)
    print('\n*****************************************************')
    print(str(a)+'.'+patron%valformat)
    print('*****************************************************')
if __name__=='__main__':
    a=0
    while True:
        phrase_h()
        a=a+1
        input("enter pour avoir une autre phrase")
    