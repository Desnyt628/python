'''
##################################################################
####_#####################_#######################_###############
###| |############_######| |#####################| |##############
###| |__##_ ##_##(_)###__| |#___##___ _#__##_###_| |_## /!_/!   _#
###| '_ \| | | |######/ _` |/ _ \/ __| '_ \| |#| | __|#(=0-0=) //#
###| |_) | |_| |##_##| (_| |  __/\__ \ |#| | |_| | |_## !  _ \// #
###|_.__/#\__, |#(_)##\__,_|\___||___/_|#|_|\__, |\__|# UUC___)  #
###########__/ |#############################__/ |################
##########|___/############628#############|___/######it's a cat!#
##################################################################

d1*pi=c1                            pour trouver la circonference du robot
c2*pi=d2                            pour trouver la circonference de la roue
c1/d2=ntr(nombre de toure de roue)  pour trouver le nombre de tour de roue qui faut mettre dans le programme
d1                                  distance entre les deux roue
c1                                  la circonference du robot
c2                                  circonference de la roue
d2                                  distance parcouru en un tour de roue
'''
###constante
pi=3.14159265359  

###modul
def rotation():
    d1=float(input('diametre entre les deux roue : '))
    c2=float(input("circonference de la roue: "))
    c1=pi*d1
    d2=c2*pi
    NTR=str(c1/d2)
    print(NTR)
    print('nombre de tour necesaire: '+NTR)
    
def tour():
    d1=float(input('diametre entre les deux roue : '))
    c2=float(input("circonference de la roue: "))
    c1=2*pi*d1
    d2=c2*pi
    NTR=str(c1/d2)
    print(NTR)
    print('nombre de tour necesaire: '+NTR)
    
def avance():
    a=float(input('distance a fair: '))
    c2=float(input("circonference de la roue: "))
    d2=c2*pi
    NTR=str(a/d2)
    print(NTR)
    print('nombre de tour necesaire: '+NTR)

###main
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
while True:
    a=0
    print('option:\n1.rotation sur une roue\n2.rotation sur lui meme\n3.avancer')
    a=input('option: ')
    if int(a)==1:
        tour()
        print('\n')
    elif int(a)==2:
        rotation()
        print('\n')
    elif int(a)==3:
        avance()
        print('\n')
    else:
        print('choisi une option valide')