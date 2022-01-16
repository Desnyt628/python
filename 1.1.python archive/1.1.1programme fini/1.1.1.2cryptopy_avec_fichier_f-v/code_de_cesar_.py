print("###################################################################")
print("####_#####################_#######################_################")
print("###| |############_######| |#####################| |###############")
print("###| |__##_ ##_##(_)###__| |#___##___ _#__##_###_| |_## /!_/!   _##")
print("###| '_ \| | | |######/ _` |/ _ \/ __| '_ \| |#| | __|#(=0-0=) //##")
print("###| |_) | |_| |##_##| (_| |  __/\__ \ |#| | |_| | |_## !  _ \// ##")
print("###|_.__/#\__, |#(_)##\__,_|\___||___/_|#|_|\__, |\__|# UUC___)  ##")
print("###########__/ |#############################__/ |#################")
print("##########|___/############628#############|___/#######it's a cat!#")
print("###################################################################")
print("")
####################code de cesar v-f   22 aout 2020 -  2020
###import
import string
###constante 
NOMFIC_IN="message_a_crypter.txt"
NOMFIC_OUT="message_crypter.txt"
s=string.printable[:-5]
CESARE=s[-3:]+s[:-3]
dic_c={}
dic_d={}
for i,k in enumerate(s):
    v=CESARE[i]
    dic_c[k]=v                                                 #dictionnaire qui chiffre 
    dic_d[v]=k                                                 #dictionnaire qui dechifre
for c in string.printable[-5:]: 
    dic_c[c] = c
    dic_d[c] = c
###fonction
def chiffrer(txt_clair,dictionaire_chiffrer):
    txt=[]
    for k in txt_clair:
        v=dic_c[k]
        txt.append(v)
        txt2="".join(txt) 
    return txt2 #txt2=message chiffrer
def  dechiffre(txt_chiffrer,dictionaire_dechiffrer):
    txt=[]
    for k in txt_chiffrer:
        v=dic_d[k]
        txt.append(v)
        txt1="".join(txt)
    return txt1 #txt1=message dechiffrer
###main
print("*** Projet Cryptopy, version 5 ***\n")
while True:

#    txt_ilisible=chiffrer(txt_u,dic_c)
#    txt_lisible=dechiffre(txt_u,dic_d)
#    print('text dechiffrer => '+txt_ilisible)
#    print('text chiffrer => '+txt_lisible)
#    print("")
#    
    with open(NOMFIC_IN,'r') as fic_lect:
        message = fic_lect.read()

    textcliare2 = ('text dechiffrer => '+dechiffre(message,dic_d))
    textesecret = ('\ntext chiffrer => '+chiffrer(message,dic_c))
    
    with open(NOMFIC_OUT,'w') as fic_ecri:
        fic_ecri.write(textcliare2)
        fic_ecri.write(textesecret)
        
    input()