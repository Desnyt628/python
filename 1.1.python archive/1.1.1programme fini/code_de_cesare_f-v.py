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
################code de cesare v-f   24 aout 2020-26 aout 2020
###import
import string
###variable 
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
def dechiffre (txt_chiffrer,dictionaire_dechiffrer):
    txt=[]
    for k in txt_chiffrer:
        v=dic_d[k]
        txt.append(v)
        txt1="".join(txt)
    return txt1 #txt1=message dechiffrer
###main
while True:
    print("")
    print("projet message coder en code cesar\n")
    txt_u=input("message a chiffrer/dechiffrer: ") #text_utilisateur
    txt_ilisible=chiffrer(txt_u,dic_c)
    txt_lisible=dechiffre(txt_u,dic_d)
    print('text dechiffrer => '+txt_ilisible)
    print('text chiffrer => '+txt_lisible)
