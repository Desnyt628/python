"""Cryptopy Version 5 (Fichiers)
Crypte et decrypte un texte en chiffrement Cesar.
Sait travailler avec le contenu d'un fichier texte.
Brendan Scott, 2015 VF par OE
"""

#### Imports
import string

#### Constantes
JEUCAR = string.printable[:-5]
CARSUBSTI = JEUCAR[-3:]+JEUCAR[:-3]

# Generation du dictionnaire avec les deux jeux de caracteres
# (en clair et substitutions).
DICO_ENCRYP = {}
DICO_DECRYP = {}
for i,k in enumerate(JEUCAR):
    v = CARSUBSTI[i]
    DICO_ENCRYP[k] = v
    DICO_DECRYP[v] = k
# Les autres  \t, \n etc. restent tels quels
for c in string.printable[-5:]: # Attention aux deux points
    DICO_ENCRYP[c] = c
    DICO_DECRYP[c] = c

MSG_TEST = "J'adore les Monty Python. Trop lol."
NOMFIC_IN  = "cryptopy_in.txt"
NOMFIC_OUT = "cryptopy_out.txt"

#### Fonctions
def encrypter(texteclair, vardico_cryp):
    """ Crypte le message texteclair avec le dictionnaire
    fourni et renvoie le texte une fois rendu illisible. """
    textesecret = []
    for k in texteclair:
        v = vardico_cryp[k]
        textesecret.append(v)
    return ''.join(textesecret)

def decrypter(textesecret, vardico_decryp):
    """ Decrypte le message textesecret avec le dictionnaire
    # fourni et renvoie texteclair."""
    texteclair = []
    for k in textesecret:
        v = vardico_decryp[k]
        texteclair.append(v)
    return ''.join(texteclair)

if __name__ == "__main__":
    print("we are a main programe")
    print("*** Projet Cryptopy, version 5 ***\n")
    with open(NOMFIC_IN,'r') as fic_lect:
         message = fic_lect.read()
         
    textesecret = encrypter(message, DICO_ENCRYP)
    print(textesecret) # Pour tester

    with open(NOMFIC_OUT,'w') as fic_ecri:
        fic_ecri.write(textesecret)
else:
    print('we are not a main programe')
     
