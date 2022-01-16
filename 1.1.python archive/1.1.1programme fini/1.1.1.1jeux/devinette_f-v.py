"""JeuDevinette.py final version"""   
"""fini 5 aout 2020"""
import random
QUITTER=-1
QUIT_TXT='e'
CREDITS="programmed by: desnyt^-^"
QUIT_MSG = "Merci  d'avoir jouer a mon premier jeux !"
QUIT_CONFIRMER = "Es-tu certain de vouloir quitter (O/n) ?"
INVITE = 'Propose un nombre : '
### COIN DES DEF###
def confirmer_quitter():
    """ On sort seulement si saisie de la
    lettre n minuscule par renvoi de False. """
    confi=input(QUIT_CONFIRMER)
    if confi == 'n':
        return False
    else:
        return True
def cat_logo():
	print("#############")
	print("# /!_/!   _##")
	print("#(=0-0=) //##")
	print("# !  _ \// ##")
	print("# UUC___)  ##")
	print("#############")
	print("#it's a cat!#")
def by_desnyt():
	print("###################################################################")
	print("####_#####################_#######################_################")
	print("###| |############_######| |#####################| |###############")
	print("###| |__##_ ##_##(_)###__| |#___##___ _#__##_###_| |_## /!_/!   _##")
	print("###| '_ \| | | |######/ _` |/ _ \/ __| '_ \| |#| | __|#(=0-0=) //##")
	print("###| |_) | |_| |##_##| (_| |  __/\__ \ |#| | |_| | |_## !  _ \// ##")
	print("###|_.__/#\__, |#(_)##\__,_|\___||___/_|#|_|\__, |\__|# UUC___)  ##")
	print("###########__/ |#############################__/ |#################")
	print("##########|___/############628#############|___/######it's a cat!##")
	print("###################################################################")
def jouer_tour():
    """ Choisit un nombre, demande au joueur
    de le trouver et reboucle tant qu'il ne l'a
    pas trouver."""
    nbr_secret=random.randint(1,100)
    nbr_saisies=0                      #AJOUT
    while True:
        nbr_joueur=input(INVITE)
        # AJOUT BLOC IF POUR SORTIE CONFIRMEE
        if nbr_joueur == QUIT_TXT:
            if confirmer_quitter():
                return QUITTER
            else:
                continue             #Tour de boucle suivant
        nbr_saisies=nbr_saisies + 1  #AJOUT
        if nbr_secret==int(nbr_joueur):
            print('Correct!')
            return nbr_saisies         #MODIF
        elif nbr_secret>int(nbr_joueur):
            print('le nombre secret est plus grand')
        else:
            print('le nombre secret est plus petit')

### SECTION PRINCIPALE MAIN
total_tours   = 0          #AJOUT
total_saisies = 0          #AJOUT
by_desnyt()
print("")
print("")
print("")
print('***pese sur "e" pour quitter***')
print("")
while True:
    total_tours=total_tours+1                   #AJOUT
    print("On passe au tour "+str(total_tours))   #MODIF
    print("essayer de trouver le nombre entre 1 et 100!")

    ce_tour=jouer_tour()    #MODIF
    #code pour fair quitter
    if ce_tour==QUITTER:
        total_tours=total_tours - 1
        if total_tours==0:
            msg_stat="ta pas faite un seul tour!!!"
        else:
            moy = str(total_saisies / float(total_tours))
            msg_stat = "Tu as fait " + str(total_tours) +\
                    " tours. Moyenne de " + str(moy)+" essai par tour."
        break
    total_saisies=total_saisies+ce_tour         #AJOUT
    print("Tu as fait "+str(ce_tour)+" saisies.") #AJOUT
    moy = str(total_saisies / float(total_tours))   #AJOUT
    print("Ta moyenne de saisies/tour = " + moy)    #MODIF
    print("")
print("")
print(msg_stat)
print("")
print("credit:")
cat_logo()
print(CREDITS)
print(QUIT_MSG)
input("appui sur enter quand tu auras lus ta moyen.")